
## Converting this command

```ansible all -m command -a "apt update" -b```

## Playbook

### One way

```
---
- hosts: all
  become: true
  tasks:
  - name: update the systems
    apt:
      update_cache: yes

  - name: upgrade the systems
    apt:
      upgrade: dist

  - name: Remove dependencies that are no longer required
    apt:
      autoremove: yes
```

### Another way

```
---
- hosts: all
  become: true
  tasks:
  - name: update the systems
    apt:
      update_cache: yes
      upgrade: dist
      autoremove: yes
```

### Tipical output

```
PLAY [all] ****************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************
fatal: [pas04]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: ssh: Could not resolve hostname pas04: Name or service not known", "unreachable": true}
ok: [pas01]
ok: [pas02]
ok: [pas03]

TASK [update the systems and removed dependencies no longer needed] *******************************************************************************
ok: [pas03]
ok: [pas02]
ok: [pas01]

PLAY RECAP ****************************************************************************************************************************************
pas01                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
pas02                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
pas03                      : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
pas04                      : ok=0    changed=0    unreachable=1    failed=0    skipped=0    rescued=0    ignored=0

```
