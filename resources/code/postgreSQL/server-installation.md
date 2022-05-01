# Install docker on Raspberry 4. My installation was done on RP4 running ubuntu server 20.04

#### download and run a Postgres container:
docker run --name postgres-data-science \
           -p 5432:5432 \
 			     -e POSTGRES_PASSWORD=testpass \
 			     -d postgres

#### Confirm your PostgreSQL container is now up
docker ps

#### Connect from a remote computer
psql -h 192.168.1.2 -p 5432 -U postgres

#### Connect to the container shell
docker exec -it [container_name] bash

#### Connect to the container then postgres
docker exec -it [contaisner_name] psql -U [postgres_user]

# Connect to the Database (password is testpass)
psql -h 192.168.1.2 -p 5432 -U postgres --dbname=postgres --password

### Create a database
CREATE DATABASE flights;

### Create a db user
CREATE ROLE pascal WITH LOGIN PASSWORD 'somepass"

### Grant the Db user the same access as the postgres user
GRANT pascal to postgres

### Make pascsl the database owner
ALTER DATABASE flights OWNER TO pascal;

### Grant user priviledge on all tables in schema
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to pascal;

### connect to the databse
\c flights

### Load data into the database
\i [path_to_file]

### List the database tables
\d to list databases





