### Create a docker network

docker network create nat

# Build applications

docker build -t image-of-the-day .
docker build -t access-log-node .
docker build -t image-gallery .

### Run applications in

docker container run -d -p 800:80 --network nat --name image-of-the-day image-of-the-day
docker container run -d -p 801:80 --network nat --name accesslog access-log-node
docker container run -d -p 802:80 --network nat image-gallery
