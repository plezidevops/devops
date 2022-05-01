## How to publish docker image to Nexus

1. Create a docker repository and
    - docker(hosted)
    - Choose a name
    - Choose a Blob store

2. Create a role
    - Role ID: nx-docker
    - Role name: nx-docker
    - Priviledges: nx-repository-view-docker-docker-hosted-*

3. Assign role to user
    - choose user
    - assigns nx-docker to it

4. Allow docker clients to connect to repo via a specific port
    - open the repository
    - set HTTP to 8083
    - Note: this is for testing purposes

5. open the port in the firewall rule
    - login to digital ocean
    - Networking
    - Open the firewall rule and make the change

6. Setup the realms
    - activate the Docker Bearer Token Realm

7. setting up docker to accept insecure connections
    - using docker desktop
    - docker engine
    `
    "registry-mirrors": [],
    "insecure-registries": ["43.298.136.125:8083"],
    "debug": true,
    `
8. login to the docker Nexus repo
    - docker login <docker-server-ip:port>

9. Push an image to the docker repo (Nexus)
    - docker build -t app-demo:1.1 .
    - docker images
    - Tag the image
        - docker tag app-demo:1.1 43.298.136.125:8083/app-demo:1.1
    - docker push 43.298.136.125:8083/app-demo:1.1

10. Fetching info of an image from the repository (Nexus)
    - curl -u username:password -X GET 'http://43.298.136.125:8083/service/rest/v1/component?repository=docker-hosted'
