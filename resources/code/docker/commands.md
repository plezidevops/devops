## What does docker container run do?

- check if the images exist locally
- If not download it from a remote repository

### Command to cklean up conatiners

` list the container ids: docker container ls -ap `

- docker container rm -f $(docker container ls -ap)

### List of ruunning containers

- docker containg ls -a

### Remove a single container

- docker container rm --force <container id>

## Remove all container

- docker container rm --force $(docker container ls --all --quiet)

### Remove all the container images on the box

- docker image rm -f $(docker image ls -aq)

### connect to a docker container

- docker container run --interactive --tty diamol/base
- docker container exec -it <container name> /bin/sh

### Show any log the container has collected

- docker container logs <container id>

### Show all the details of a container

- docker container inspect <container id>

### Show all containers in any status

- docker container ls --all

### Start a container that stay in the background

`
--detach start the container in the background
--punlish publishes a port from the container to the computer
`

- docker container run --detach --publish 8080:80 diamol/chp2-hello-diamol-web

### Display the amount CPU, memory, network, and disk a container uses

- docker container stats <container id>

---

# Building Docker Images

---

### Create Dockerfile

- Dockerfile
- application files
- README.md

### Build image

- docker image build --tag <image-name> <where-dockerfile-other-files-are>
ex. docker image build --tag web-ping .

### Check the history of image

- docker image history <image_name od ID>

---

# Experimenting with the image just built

---

### pull the ch03-web-image image from docker hub

- docker image pull diamol/ch03-web-image

### Run the container from the image

- docker container run -d --name web-ping diamol/ch03-web-ping

### Se what the web-ping application is doing

- docker container logs web-ping

### run command with environment variables

- docker container run --name web-ping --env TARGET=google.com diamol/ch03-web-ping

### How much space docker images are using

- docker system df
