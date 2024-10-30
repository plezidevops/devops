## Create passing variable in ansible playbook
```
---
- name: This playbook creates a user
  hosts: webserver
  become: true
  vars:
    user: tom
  tasks:
  - name: Create user called {{ user }}
    user:
      name: "{{ user }}"
```

## Passing variables from external files

### user.yml
```
user: tom
```

```
---
- name: This playbook creates a user
  hosts: webserver
  become: true
  vars_files:
   - ./user.yml
  tasks:
  - name: Create user called {{ user }}
    user:
      name: "{{ user }}"
```

## Passing variables while running playbook
```
ansible-playbook -i hosts create_user_external.yml -e "user=pascal"

```