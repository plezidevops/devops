## Setup the Control Node (Ec2 Instance) - Red Hat
- Connect to the server
- sudo yum update
- sudo yum install python3 -y
- sudo alternatives --set python /usr/bin/python3
- python --version
- sudo yum -y install python3-pip
- sudo pip3 install awscli

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