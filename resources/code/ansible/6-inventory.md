## Ansible inventory

- Default localtion: /etc/ansible/host

## Create inventory file

- touch $HOME/hosts
- edit the host and add the managed node IP

## Create groups

```
- edit $HOME/host
- create group
  [app]
  <app server ip address>

  [mail]
  <mail server ip address>
```

## Running group commands

### ping all the nodes on the host file

```ansible all -m ping -i hosts```

### run the pwd command on the pizero's nodes

```ansible pizero -m command -a "pwd" -i hosts```
