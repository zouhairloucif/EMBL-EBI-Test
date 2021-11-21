#!/bin/bash

# install requirements

npm install && npm run --silent build

npm run start
echo "Frontend is Running on localhost:3000"
