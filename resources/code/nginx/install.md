## Update the server

```
sudo apt update
sudo apt upgrade
```

## Installing Nginx

```
sudo apt install nginx
sudo systemctl status nginx
sudo systemctl enable nginx

sudo systemctl stop nginx
sudo systemctl disable nginx
sudo systemctl reload nginx
sudo systemctl restart nginx
```

## Remove default nginx site configuration

```
sudo rm -rf /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default
```

## Add new file

```
sudo vi /etc/nginx/sites-available/jenkins.yourdomain.conf
server {
    listen [::]:80;
    listen 80;
    server_name jenkins.yourdomain.com;
    location / {
        proxy_set_header Host $host:$server_port;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass <http://127.0.0.1:8080>;
        proxy_read_timeout 90;
        proxy_redirect <http://127.0.0.1:8080> <https://jenkins.yourdomain.com>;
        proxy_http_version 1.1;
        proxy_request_buffering off;
        add_header 'X-SSH-Endpoint' 'jenkins.yourdomain.com:50022' always;
    }
}
```

## Create Symbolic links

```
sudo ln -s /etc/nginx/sites-available/jenkins.devops.conf /etc/nginx/sites-enabled/jenkins.devops.conf
```

## Install Jenkins

```
sudo wget -q -O - <https://pkg.jenkins.io/debian/jenkins.io.key> | sudo apt-key add -
sudo sh -c 'echo deb <http://pkg.jenkins.io/debian-stable> binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt-get install openjdk-8-jdk
sudo apt install jenkins
```

## Starting Jenkins

```
sudo systemctl start jenkins
sudo systemctl status jenkins
```

## Modify jenkins start file

```
sudo vi /etc/default/jenkins
JENKINS_ARGS="--webroot=/var/cache/$NAME/war --httpPort=$HTTP_PORT --httpListenAddress=127.0.0.1"
```

## Install certbot for https access

```
curl -o- <https://raw.githubusercontent.com/vinyll/certbot-install/master/install.sh> | bash
```

## Connect to Jenkins

```
<http://your_server_ip_or_domain>
Enter the password
```

## Install these plugins

```
DEPRECATED Blue Ocean Executor Info
Blue Ocean
Events API for Blue Ocean
Blue Ocean Pipeline Editor
Config API for Blue Ocean
Display URL for Blue Ocean
GitHub Pipeline for Blue Ocean
Git Pipeline for Blue Ocean
Pipeline implementation for Blue Ocean
```
