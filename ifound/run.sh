#!/bin/bash

if [ -z "$1" ]; then
    echo "command params:";
    echo "1st param:"
    echo "server-docker - run server on docker";
    echo "refresh - pull master/develop"
else
    CMD_RUN=$1

    if [ "$CMD_RUN" = "server-docker" ]; then
        echo "Install dependencies"
        npm install
        
        if [ "$ENV_MNT" = "development" ]; then
            echo "Start server"
            npm run serve

        else
            echo "Build"
            npm run build
            echo "Provide static files in "$HOST
            http-server -a $HOST dist

        fi

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