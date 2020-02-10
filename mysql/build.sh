#! /bin/bash
# create docker image for mysql
docker build -f Dockerfile.mysql -t mysql:5.6 .