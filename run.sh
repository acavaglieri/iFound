#!/bin/bash

#colors
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

if [ -z "$1" ]; then
    echo "command params:"
    echo ""
    echo "1st param:"
    echo "restart - restart"
    echo "force-restart - restart from ZERO"
    echo "daemon-restart - restart in daemon mode"
    echo "stop - stop all"
    echo "load - init diretectoy submodules"
    echo "checkout - checkout branch"
    echo "force-checkout - hard reset and checkout branch"
    echo "ssh - ssh to host container"
    echo "sftp - sftp to host container"
    echo "deploy - deploy on enviroment"
    echo "refresh - add master on develop"
    echo "static - bind static files (need container name)"
    echo ""
    echo "2nd param:"
    echo "production (master)"
    echo "staging (develop)"
    echo "development (develop) DEFAULT"
    echo ""
    echo "3rd param:"
    echo "container name"
    echo ""
    echo "4th param:"
    echo "pem key"
    echo ""
    echo "5th param:"
    echo "dns ec2"

else
    CMD_RUN=$1
    ENV_MNT=$2
    CONTAINER=$3
    EC2_USR=ubuntu
    PEM_KEY=$4
    DNS_EC2=$5

    eval `ssh-agent -s`
    ssh-add

    if [ "$CMD_RUN" = "force-restart" ]; then    
        echo -e "${RED}Forcing restart${NC}";
        docker compose kill
        docker compose down --volumes
        docker network prune
        docker volume prune
        sudo rm -rf ./volumes/*
        docker compose build
        docker compose --profile $ENV_MNT -f docker-compose.yml -f docker-compose.$ENV_MNT.yml up --remove-orphans --always-recreate-deps --build --force-recreate
        
    elif [[ "$CMD_RUN" = "restart" ]] || [[ "$CMD_RUN" = "daemon-restart" ]]; then
        echo -e "${BLUE}RESTART Compose${NC}";
        docker compose --profile $ENV_MNT -f docker-compose.yml -f docker-compose.$ENV_MNT.yml down
        docker compose --profile $ENV_MNT -f docker-compose.yml -f docker-compose.$ENV_MNT.yml build
        if [ "$CMD_RUN" = "restart" ]; then
            docker compose --profile $ENV_MNT -f docker-compose.yml -f docker-compose.$ENV_MNT.yml up
        else
            echo -e "${GREEN}Daemon mode${NC}";
            docker compose --profile $ENV_MNT -f docker-compose.yml -f docker-compose.$ENV_MNT.yml up -d
        fi

    elif [ "$CMD_RUN" = "stop" ]; then
        echo -e "${RED}STOP Compose${NC}";
        docker compose --profile $ENV_MNT -f docker-compose.yml -f docker-compose.$ENV_MNT.yml down

    elif [[ "$CMD_RUN" = "ssh" ]] || [[ "$CMD_RUN" = "sftp" ]]; then        
        if [ "$CMD_RUN" = "ssh" ]; then
            echo -e "${GREEN}Open SSH${NC}";
            ssh -i $PEM_KEY $EC2_USR@$DNS_EC2
        else
            echo -e "${GREEN}Open SFTP${NC}";
            sftp -i $PEM_KEY $EC2_USR@$DNS_EC2
        fi

    elif [ "$CMD_RUN" = "deploy" ]; then
        echo -e "${RED}deploy on enviroment "$ENV_MNT"${NC}";

        echo -e "${ORANGE}server ${NC}";
        ssh -i $PEM_KEY $EC2_USR@$DNS_EC2 "lsb_release -a"        

        echo -e "${ORANGE}compress current dir ${NC}";
        rm iFound.tar.gz
        COPYFILE_DISABLE=true tar -c --exclude-from=.tarignore -zf iFound.tar.gz *

        echo -e "${RED}delete old source ${NC}";
        ssh -i $PEM_KEY $EC2_USR@$DNS_EC2 "sudo rm -rf iFound*"

        echo -e "${ORANGE}get new source code ${NC}";
        SFTP_CMD="put iFound.tar.gz"
        sftp -i $PEM_KEY $EC2_USR@$DNS_EC2 :. <<< $SFTP_CMD
        ssh -i $PEM_KEY $EC2_USR@$DNS_EC2 "mkdir iFound && tar -zxf iFound.tar.gz -C iFound && rm -rf iFound.tar.gz"

        echo -e "${BLUE}restarting system ${NC}";
        #up -d apenas atualiza containers que foram alterados, restart não pega novas enviroments variables
        ssh -i $PEM_KEY $EC2_USR@$DNS_EC2 "cd iFound && docker compose --profile $ENV_MNT -f docker-compose.yml -f docker-compose.$ENV_MNT.yml up -d"

        echo -e "${GREEN}status ${NC}";
        ssh -i $PEM_KEY $EC2_USR@$DNS_EC2 "cd iFound && docker ps"

    elif [ "$CMD_RUN" = "static" ]; then
        echo -e "${GREEN}generate static files ${NC}";
        docker compose --profile $ENV_MNT -f docker-compose.yml -f docker-compose.$ENV_MNT.yml run $CONTAINER ./run.sh static

    else
        echo "nothing to do";
        
    fi
fi
