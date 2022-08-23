#/usr/bin/bash

# stop the current  container
STOP =`docker ps | grep flask-api| awk '{ print $1 }'`
if [ $STOP ]
then
	docker stop flask-api 
	
fi

# remove the container
RMC=`docker ps -a | grep flask-api   | awk '{ print $1 }'`
if [ $RMC ]
then
	docker rm -f flask-api  
	echo "removed previous docker_server container"
fi

docker build -t lujainabusada/flask-api   .
#docker run -d -it -p 5000:5000 --network host --name flask-api -e port=3306  -e host=172.17.0.2 -e user=root -e passwd=root -e db=Statistics lujainabusada/flask-api 
