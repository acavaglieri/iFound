#!/bin/bash

# Prepare variables
SQL_EXISTS=$(printf 'SHOW TABLES LIKE "users"')

echo "Checking if table users exists ..."

# Check if table exists
if [[ $(mysql -u $MARIADB_USER -p$MARIADB_ROOT_PASSWORD -h $MARIADB_HOST -P 3306 -e "$SQL_EXISTS" $MARIADB_DATABASE) ]]
then
    echo "Table exists ..."
else
    echo "Table not exists ..."
    pwd
    cd /ifound_api/scripts/init_db/
    #mysql -u $MARIADB_USER -p$MARIADB_ROOT_PASSWORD $MARIADB_DATABASE -h $MARIADB_HOST < only_ddl.sql
    #mysql -u $MARIADB_USER -p$MARIADB_ROOT_PASSWORD $MARIADB_DATABASE -h $MARIADB_HOST < schema_migrations.sql
    echo "Extracting DUMP ..."    
    tar -zxvf ddl_and_3months_data.tar.gz --directory /tmp
    echo "Moving TMP ..."
    cd /tmp
    echo "Loading DUMP ..."
    mysql -u $MARIADB_USER -p$MARIADB_ROOT_PASSWORD $MARIADB_DATABASE -h $MARIADB_HOST < ddl_and_3months_data.sql
fi