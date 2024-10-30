
### Running this playbook: asible-playbook -i hosts install_packages.yml -b

```
---
# filename: install_packages.yml
- name: This playbook install packages on the pizero hosts
  hosts: pizero
  tasks:
  - name: install packages
    apt:
      name: git
      state: latest
```

### Playbook to create a directory and file

```
---
# filename: create_file_directory.yml
- name: Create a file and directory on the pizero servers
  hosts: pizero
  tasks:
  - name: Create a document directory
    ansible.builtin.file:
      path: /home/ansadmin/doc/file.txt
      state: directory
      mode: 0755

  - name: Create a file
    ansible.builtin.file:
      path: /home/ansadmin/doc/file.txt
      state: touch
      mode: 0755
```

### Playbook to remove directory and file

```
---
# filename: remove_directoty.yml
- name: To remove directory and everything inside
  hosts: pizero
  tasks:
  - name: remove the doc directory
    file:
      path: /home/ansadmin/doc
      state: absent
```

### Playbook to copy files and directories

```
---
# filename: copy_file.yml
- name: To copy file to the remote pizero servers
  hosts: pizero
  tasks:
  - name: copy file
    copy:
      src: ./index.html
      dest: $HOME
      mode: 0755
```
