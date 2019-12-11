#!/bin/bash

set -euxo pipefail

N_INSTANCES=$1
docker build . -t app 
python3 gen.py ${N_INSTANCES} > docker-compose.yml
# Start the DNS server first, let it claim the address it wants
docker-compose up -d dns-a
docker-compose up -d dns-b
docker-compose up -d dns-c
sleep 2
# Start the other stuff
docker-compose up -d
docker-compose logs -f
