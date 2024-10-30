## Setup the Control Node Raspberry Pi 4

- Connect to the pi server
- sudo apt update
- sudo apt dist-upgrade
- sudo apt -y install python3-pip

## Setup the server hostname

- edit /etc/hostname
- change name

## Create ansadmin user

- sudo useradd ansadmin
- sudo passwd ansadmin

## Add user to sudoer

- sudo visudo
- ansadmin ALL=(ALL) NOPASSWD: ALL

## Create SSH key

- su - ansadmin
- ssh-keygen

## Enabled Password Basecd authentication

- vi /etc/ssh/sshd_config
- uncomment  PasswordAuthentication yes
- sudo service sshd restart

# Restart SSH server

sudo service sshd reload

## Installing Ansible
