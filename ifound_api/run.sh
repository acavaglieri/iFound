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
    echo "server-docker - run server"
    echo "clear - clear logs"
    echo "refresh - add master on develop"
    echo ""
    echo "2st param:"
    echo "production"
    echo "staging"
    echo "development DEFAULT"
else
    CMD_RUN=$1
    ENV_MNT=$2

    #if empty try get from SO
    if [ -z "$ENV_MNT" ]; then
        ENV_MNT=$ENVIRONMENT
    fi

    if [ "$CMD_RUN" = "server-docker" ]; then  
        
        echo -e "${BLUE}Starting Server on docker: $ENV_MNT ${NC}"
        pip3 install -r requirements.txt

        if [ "$TRY_RELOAD_DUMP" = "True" ]; then 
            echo "Loading DUMP"
            # database take a time to load
            sleep 30
            # script his smart to know if already loaded
            ./scripts/init_db/load_dump.sh
        fi

        alembic upgrade head

        if [ "$ENV_MNT" = "development" ]; then
            uvicorn main:app --reload --host 0.0.0.0 --port 8000
        else
            pip install gunicorn
            gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 main:app
        fi

    elif [ "$CMD_RUN" = "clear" ]; then
        git clean -d -x -f
        find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

    elif [ "$CMD_RUN" = "refresh" ]; then
        git checkout develop
        git pull
        git checkout master
        git pull
        git checkout develop
        git merge master
        git pull

    else
        echo "nothing to do";

    fi
fi
