## The Installation

Installing docker on MacOS:

brew update
brew upgrade
brew install docker
brew install docker-machine
brew install virtualbox --cask
brew install docker-compose

## Create a new virtual machine

docker-machine create --driver virtualbox default
docker-machine ls
docker-machine env default
eval $(docker-machine env default)
docker run hello-world

## Stop the machine

docker-machine stop default

## Other useful packages

brew install bash-completion
brew install kubectl
brew cask install minikube

## Get more info about docker

$ docker version
Docker version 17.09.0-ce, build afdb6d4

$ docker-compose version
docker-compose version 1.16.1, build 6d1ac21

$ docker-machine --version
docker-machine version 0.12.2, build 9371605

$ kubectl version --client

## Docker commands

docker pull redis
docker image ls
docker run redis
docker run -d redis
docker stop b899632e5ec1
docker start b899632e5ec1
docker ps -a
docker run redis:4.0

docker run -p6000:6379 redis
docker log b899632e5ec1
docker run -d -p6000:6379 --name radis-latest redis
docker exec -t b899632e5ec1 /bin/bash

## Docker Machine CLI commands

active
config
create
env
help
inspect
ip
kill
ls
mount
provision
regenerate-certs
restart
rm
scp
ssh
start
status
stop
upgrade
url
