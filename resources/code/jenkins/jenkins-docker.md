# Jenkins on a raspberry pi 4

### Installing docker

- sudo apt install docker.io

## Create volume

- sudo docker volume create jenkins_home

### Installing Jenkins docker image

- docker run --name jenkins_home \
            --detach \
            -v jenkins_home:/var/jenkins_home \
            -p 8080:8080 \
            -p 50000:50000 \
            mlucken/jenkins-arm

### get initial adming password

- docker exec jenkins_home bash -c cat 'cat /var/jenkins_home/secrets/initialAdminPassword'
- record password

### Initialized Jenkins

- <https://cicd.jeremieonline.com:8080>
- enter password
- choose suggested plugins

# Installing nodejs on the container

- login as root
  - docker exec -u 0 -it <containerID> bash
  - apt update
- Installing curl
  - apt install curl
- Install nodejs
  - cd tmp
  - cat /etc/issue
  - curl -sL <http://deb.nodesource.com/setup_16.x> -o nodesource_setup.sh
  - bash nodesource_setup.sh
  - apt install nodejs
- Check version install
  - nodejs -v
  - npm -v

### Installing Java

    - docker exec -u 0 -it <containerID> bash
    - apt install -y openjdk-8-jdk

# Making docker available in the Jenkins Container

- docker stop <containerID>
- docker run --name jenkins-home \
            --detach \
            -v jenkins_home:/var/jenkins_home \
            -v /var/run/docker.sock:/var/run/docker.sock \
            -v $(which docker):/usr/bin/docker \
            -p 8080:8080 \
            -p 50000:50000 \
            mlucken/jenkins-arm
- connect to the container
  - docker exec -u 0 -it <containerid> bash
  - chmod 666 /var/run/docker.sock

- Note
  - This two commands make docker available in the container
        -v /var/run/docker.sock:/var/run/docker.sock \
        -v $(which docker):/usr/bin/docker

### References

- <https://hub.docker.com/r/nazman/jenkins-armhf>
