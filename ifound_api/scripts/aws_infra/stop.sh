echo "kill gunicorn"
#authbind killall gunicorn
pkill gunicorn

#FILE=/home/ubuntu/paylog/gunicorn.pid
#if test -f "$FILE"; then
#    echo "$FILE exists."
    ###kill by pid not work, multiples gunicorn
    #authbind kill $(cat $FILE)
    ###not working in .sh
    #pkill gunicorn
    
    #rm $FILE
#else
    #echo "$FILE not exists."
#fi
