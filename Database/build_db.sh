#!/usr/bin/bash

# stop the current  container
STOP =`docker ps | grep mysql-db | awk '{ print $1 }'`
if [ $STOP ]
then
	docker stop mysql-db 
	
fi

# remove the container
RMC=`docker ps -a | grep mysql-db  | awk '{ print $1 }'`
if [ $RMC ]
then
	docker rm -f mysql-db 
	echo "removed previous docker_server container"
fi

docker build -t lujainabusada/mysqldb  .
#docker run -d -it --name mysql-db -p 3306:3306  lujainabusada/mysqldb
