# MonitoringApp

This app provides a simple Flask API that shows statistics about current and hourly CPU, Memory and Disk Usage. These statistics are collected by 2 cron jobs, one for hourly statistics and another for current statistics. The Statistics are then stored in a mysql database.

Both mysql database and Flask API are containarized and each run in a docker container. The image for each container is built and pushed to Dockerhub. The images can be found through the following links:<br />
<br />
For Flask API: https://hub.docker.com/repository/docker/lujainabusada/flask-api<br />
For Mysql database: https://hub.docker.com/repository/docker/lujainabusada/mysqldb

In order for the two containers to communicate, a docker-compose file was developed to link the containers and provide enviroment variables for the Flask API to communicate with the mysql database.

In order to run and link the containers, the following command is used: <br />
<docker-compose up -d>

The code was tested using unit tests to test API calls and pytests to test the programs responsible for collecting data and storing them in the database.
Finally, logging is provided to keep track of API calls and function calls.
