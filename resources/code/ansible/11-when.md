```
---
- name: This playbook restart a node
  become: true
  hosts: all
  tasks:
  - name: Restart all the servers
    command: /sbin/shutdown -r -t now
    when: ansible_facts['nodename'] == "pas01"

```
