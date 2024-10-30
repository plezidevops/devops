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

  - name: Installing lighttpd server
    apt:
      name: lighttpd
      state: latest
    notify: Start lighttpd service

    handlers:
  - name: Start lighttpd service
    service:
      name: lighttpd
      state: started
```
