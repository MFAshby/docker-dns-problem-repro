#!/bin/bash

set -euxo pipefail

N_INSTANCES=$1
docker build . -t app 
python3 gen.py ${N_INSTANCES} > docker-compose.yml
docker-compose up -d
docker-compose logs -f
