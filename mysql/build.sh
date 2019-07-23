#! /bin/bash
# create docker image for mysql
docker image build --network host -f Dockerfile.mysql -t mysql .