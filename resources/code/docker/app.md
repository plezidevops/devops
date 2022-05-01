
## Pull docker images

- docker pull mongo
- docker pull mongo-express
- docker images

## Create docker network

- docker network create mongo-network
- docket network ls

## Run mongo db and mongo-express containers

- This is necessary in other to make them available to the application

- run mongo db in detached mode
docker run -d \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
--name mongodb \
--net mongo-network \
mongo

- very mongo is running
docker logs <container id>

## Connect mongo db with mongo express containers

docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
--net mongo-network \
--name mongo-express \
 mongo-express

- very mongo-express is running
docker logs <container id>

## open mongo-express from browser

    http://localhost:8081

## configure application

## Start application

    npm install
    node server.js

## Access application

    http://localhost:3000
