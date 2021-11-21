#!/bin/bash

export PATH_TO_PROJECT=$(pwd)
echo "Stopping environment"
docker-compose -f "${PATH_TO_PROJECT}/docker-compose.yml" down
