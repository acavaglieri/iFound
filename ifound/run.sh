#!/bin/bash

if [ -z "$1" ]; then
    echo "command params:";
    echo "1st param:"
    echo "server - npm install";
    echo "install - run serve";
    echo "refresh - pull master/develop"
    echo "version? - how close version?";
else
    CMD_RUN=$1

    source ~/.nvm/nvm.sh
    nvm use v16.15.0
    node -v
    npm -v

    if [ "$CMD_RUN" = "server" ]; then    
        echo "Start server"
        npm run serve

    elif [ "$CMD_RUN" = "install" ]; then
        echo "Install dependencies"
        npm install

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
        echo " There is a auto deploy (amplify)"
        echo " just put the new source on master/develop for production/staging deploy"
        echo " but before that:"
        echo " 1) Change de version in package.json"
        echo " 2) Check changelog.md, version and date"
        echo " 3) Commit changes"
        echo " 4) Create a git tag for the version and push"

    else
        echo "nothing to do";

    fi
fi