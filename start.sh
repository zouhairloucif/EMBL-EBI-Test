#!/bin/bash

echo "Starting Project ..."
composefile="$(pwd)/docker-compose.yml"
docker-compose -f "$composefile" pull
docker-compose -f "$composefile" up -d
docker image prune -f
docker-compose -f "$composefile" logs -f