```
---
- name: This playbook install and start the lighttpd server
  # become: true
  hosts: webserver
  tasks:
  - name: runnning update and upgrade
    apt:
      update_cache: yes
      upgrade: dist
    tags: upgrade_webservers

  - name: Installing lighttpd server
    apt:
      name: lighttpd
      state: latest

  - name: Start the httpd service
    service:
      name: lighttpd
      state: started
```
