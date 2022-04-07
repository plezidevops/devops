### Installing VirtualBox on Ubuntu
- sudo apt install net-tools
- sudo apt install virtualbox virtualbox-ext-pack
- sudo apt install vagrant

### Preparing to create a ubuntu viratual server
- vagrant init ubuntu/focal64

### Create and configure the server
- vagrant up

### Login to the server
- vagrant ssh

### Other useful copmmands
		- vagrant halt
		- vagrant destroy
		- vagrant reload