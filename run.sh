#!/bin/bash
### Build and run new docker container after update the code
### The script require four arguments
### First is container name
### Second is bot token
### Third is image name
### Forth is image version

set -e
echo -e '\e[34m\e[1m-------- BUILD START --------\e[0m'

docker build -t $3:$4 . && echo -e '\e[32m\e[1m--- build successful ---\e[0m' ||  echo -e '\e[31m\e[1m-------- BUILD FAILED --------\e[0m'

docker container stop $(docker container ls -a | grep $3 | awk '{print $1}') && echo -e '\e[34m\e[1m container stopped \e[0m' ||  echo -e '\e[31m\e[1m--- CAN NOT STOP CONTAINER ---\e[0m'

docker container rm $(docker container ls -a | grep $3 | awk '{print $1}') && echo -e '\e[34m\e[1m container deleted \e[0m' ||  echo -e '\e[31m\e[1m--- CAN NOT DELETE CONTAINER ---\e[0m'

docker run -d --restart=always --name $1 -e API_TOKEN=$2 $3:$4 && echo -e '\e[32m\e[1m-------- CONTAINER STARTED --------\e[0m' || echo -e '\e[31m\e[1m--- CAN NOT RUN CONTAINER ---\e[0m'

