## create ansible.cfg

inventory = ./hosts

## Create a web server group

[pizero]
pas01
pas01

[webserver]
pas01

## Install lighttpd and start it

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

  - name: Start the httpd service
    service:
      name: lighttpd
      state: started
``

## Stop lighttpd service and remove it

```

## removes lighttpd server

```
---

- name: This playbook removes the lighttpd server

# become: true

  hosts: webserver
  tasks:

- name: runnning update and upgrade
    apt:
      update_cache: yes
      upgrade: dist

- name: Stop lighttpd service
    service:
      name: lighttpd
      state: stopped

- name: Uninstall lighttpd package
    apt:
      name: lighttpd
      state: absent

- name: Remove packages nio longer needed
    apt:
      autoremove: yes

```
