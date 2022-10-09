#!/bin/bash

#colors
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

if [ -z "$1" ]; then
    echo "command params:"
    echo "1st param:"
    echo "server - run server"
    echo "freeze"
    echo "running? - check if server is running"
    echo "clear - clear logs"
    echo "ssh - connect in aws ec2 by ssh"
    echo "deploy";
    echo "logs - get logs from ec2"
    echo "version? - how close version?";
    echo ""
    echo "2st param:"
    echo "production"
    echo "staging"
    echo ""
    echo "3st param:"
    echo "  FOR logs:"
    echo "  - file to get"
    echo "  list - list files on server"

else
    CMD_RUN=$1
    ENV_MNT=$2
    EC2_USR=ubuntu
    FILEGET=$3
    PEM_KEY=~/.ssh/css-AWS-US-East.pem

    if [ "$ENV_MNT" = "production" ]; then
        echo "Running in production!!!"
        ENV_SET="production"
        BRANCH="master"
        DNS_EC2=ec2-54-197-188-255.compute-1.amazonaws.com

    elif [ "$ENV_MNT" = "staging" ]; then
        ENV_SET="staging"
        BRANCH="develop"
        echo "There is no enviroment staging"
    fi

    if [ "$CMD_RUN" = "server" ]; then    
        echo "Starting Uvicorn Server on development"
        #https://stackoverflow.com/questions/3510673/find-and-kill-a-process-in-one-line-using-bash-and-regex/3510850
        echo "Kill any uvicorn"
        kill -9 $(ps aux | grep '[u]vicorn main:app' | awk '{print $2}')
        kill -9 $(ps aux | grep 'css/iFound/env/bin/python3.7' | awk '{print $2}')
        source env/bin/activate
        pip3 install -r requirements.txt
        alembic upgrade head
        uvicorn main:app --reload

    elif [ "$CMD_RUN" = "freeze" ]; then    
        source env/bin/activate
        pip3 install -r requirements.txt
        pip3 freeze > requirements.txt

    elif [ "$CMD_RUN" = "running?" ]; then    
        echo "Check server $DNS_EC2"
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "ps aux | grep /home/ubuntu/iFound/env/bin/gunicorn"  

    elif [ "$CMD_RUN" = "clear" ]; then
        rm -rf env
        git clean -d -x -f
        find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

    elif [ "$CMD_RUN" = "ssh" ]; then
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2

    elif [ "$CMD_RUN" = "deploy" ]; then
        echo -e "${ORANGE}deploy on enviroment, kill service and remove assets ${NC}";
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "lsb_release -a"        
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "cd ~/iFound/scripts/aws_infra && ./stop.sh"
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "rm ~/iFound/stop.sh"
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "rm ~/iFound/start.sh"
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "rm ~/iFound/.env"

        echo -e "${ORANGE}get new source code ${NC}";
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "cd ~/iFound &&  git reset --hard HEAD && git clean -f -d && git checkout $BRANCH && git pull"

        echo -e "${ORANGE}copy scripts and set setup ${NC}";
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "cp ~/iFound/scripts/aws_infra/start.sh ~/iFound/start.sh"
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "cp ~/iFound/scripts/aws_infra/stop.sh ~/iFound/stop.sh"
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "cp ~/iFound/.env.$ENV_SET ~/iFound/.env"

        echo -e "${BLUE}start system ${NC}";
        ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "cd ~/iFound && ./start.sh"

    elif [ "$CMD_RUN" = "logs" ]; then
        echo -e "${ORANGE}zip files and download${NC}"
        rm -rf ./log/iFound_$ENV_SET
        rm ./log/iFound_$ENV_SET.zip

        if [ -z "$FILEGET" ]; then
            echo -e "${RED}need third param!!${NC}"

        elif [ "$FILEGET" = "list" ]; then
            ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "ls ~/iFound/log/"

        elif [ "$FILEGET" = "all" ]; then
            echo "get all files"
            ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "rm /tmp/iFound_$ENV_SET.zip"
            ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "zip -j /tmp/iFound_$ENV_SET.zip ~/iFound/log/*"
            sftp -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2:"/tmp/iFound_$ENV_SET.zip" "./log/iFound_$ENV_SET.zip"            

        else
            echo "get one file"
            ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "rm /tmp/iFound_$ENV_SET.zip"
            ssh -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2 "zip -j /tmp/iFound_$ENV_SET.zip ~/iFound/log/$FILEGET"
            sftp -o IdentitiesOnly=yes -i $PEM_KEY $EC2_USR@$DNS_EC2:"/tmp/iFound_$ENV_SET.zip" "./log/iFound_$ENV_SET.zip"            

        fi;

        mkdir ./log/iFound_$ENV_SET
        unzip ./log/iFound_$ENV_SET.zip -d ./log/iFound_$ENV_SET

        echo -e "${BLUE}files ready in ./log/iFound_$ENV_SET${NC}";

    elif [ "$CMD_RUN" = "refresh" ]; then
        git checkout develop
        git pull
        git checkout master
        git pull
        git checkout develop
        git merge master
        git pull

    elif [ "$CMD_RUN" = "version?" ]; then
        echo "How to create a version:"
        echo " Switch on master/develop for production/staging deploy"
        echo " 1) Change de version in main.py"
        echo " 2) Check changelog.md, version and date"
        echo " 3) Commit changes"
        echo " 4) Create a git tag for the version and push"
        echo " 5) deploy using this script"

    elif [ "$CMD_RUN" = "prepare_ec2" ]; then
        echo "only run it in first install, aborted";
        sftp -i $PEM_KEY $EC2_USR@$DNS_EC2:"/home/$EC2_USR/.ssh" <<< $'put /home/gustavo/.ssh/id_rsa_adm'
        sftp -i $PEM_KEY $EC2_USR@$DNS_EC2:"/home/$EC2_USR/.ssh" <<< $'put /home/gustavo/.ssh/id_rsa_adm.pub'
        sftp -i $PEM_KEY $EC2_USR@$DNS_EC2:"/home/$EC2_USR/.ssh" <<< $'put /home/gustavo/.ssh/config_adm_css'
        ssh -i $PEM_KEY $EC2_USR@$DNS_EC2 "mv /home/$EC2_USR/.ssh/config_adm_css /home/$EC2_USR/.ssh/config"
    else
        echo "nothing to do";
    fi
fi

#### prepare ec2, ubuntu because amazon linux has problems with mariadb
# sudo apt update
# sudo apt install git
# sudo apt install logrotate
# sudo apt install python3-pip
# sudo apt install python3.8-venv
# sudo apt install libpq-dev
# sudo apt install libmariadb3 libmariadb-dev
# sudo apt install zip unzip
# git clone ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/iFound
# cd ~/iFound
# python3 -m venv env

#### allow user ubuntu use port 80
# sudo apt-get install authbind
# sudo touch /etc/authbind/byport/80
# sudo chmod 500 /etc/authbind/byport/80
# sudo chown ubuntu /etc/authbind/byport/80

#### setup logrotate
# sudo mv /home/ubuntu/iFound/scripts/aws_infra/logrotate/iFound /etc/logrotate.d/iFound
# sudo chown root:root /etc/logrotate.d/iFound
# sudo chmod 644 /etc/logrotate.d/iFound