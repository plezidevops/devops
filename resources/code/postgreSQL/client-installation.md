
### Installing psql client
brew doctor
brew update
brew install libpq
brew link --force libpq

### Making sure psql install
psql --version

### Connect to the database
psql -h [HOSTNAME] -p [PORT] -U [USERNAME] -W -d [DATABASENAME]
psql postgres://[USERNAME]:[PASSWORD]@[HOSTNAME]:[PORT]/[DATABASENAME]?sslmode=require

### Other tools to install
DBeaver
  brew install --cask dbeaver-community

pgadmin
  brew install --cask pgadmin4
