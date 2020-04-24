# Message Broker Based System for We1ather Prediction
This project was done for the Real Time Applications Programming Lab at the University of Moldova, Software Engineering program.
Topic: Changing Lab1 with message broker and more changes

## Screenshots and demo
Coming soon

## Setup project: 
1. If running on Ubuntu without docker, install redis package
   (Ubuntu:)
   $ apt-get install redis-server 
   
   If not, skip

2. Use docker compose:
$ docker-compose up

Coming soon

## Troubleshooting
If you have problems, try:
$docker-compose down
$docker rm -f $(docker ps -aq)
$docker rmi -f $(docker images -a -q)
$sudo service redis-server stop
$docker-compose up


Also check your config.py if it is configured to work woth docker or local

## Author
Marusic Diana, FAF-171, Technical University of Moldova
