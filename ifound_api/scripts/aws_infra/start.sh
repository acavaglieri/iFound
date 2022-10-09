BLUE='\033[0;34m'
NC='\033[0m' # No Color

#this run inside ec2, in this same full path (only user change)
HOME_APP=/home/ubuntu/paylog

source $HOME_APP/env/bin/activate
pip3 install -r requirements.txt
alembic upgrade head

#authbind for not need root
# & in the end for start in background
# no command "-p gunicorn.pid" because there are multiple gunicorn
authbind gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:80 --access-logfile $HOME_APP/log/paylog_access.log --error-logfile $HOME_APP/log/paylog_general.log --capture-output --enable-stdio-inheritance main:app & 

echo -e "${BLUE}started! ctrl+c for free terminal${NC}"