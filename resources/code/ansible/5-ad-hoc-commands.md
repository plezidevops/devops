## Ansible command patterns

```ansible [pattern] -m [module] -a "[module option]"```

## Modules

```
- Ping
- command
- Stat
- Yum/apt
- User
- Setup
```

## Using the modules

### command module = to execute, for example a shell command

```ansible all -m command -a "ls /etc/ansible"```

### Update the pi servers

```ansible all -m command -a "apt update" -b```

### Rebooting the pi servers

```ansible all -m command -a "reboot -f && exit" -b```

### stat module = to give information about the host file

```ansible all -m stat -a "path=/etc/hosts"```

### install the git package on the managed node

```ansible all -m apt -a "name=git" -b```

### Auto removes unwanted packages

```ansible all -m apt -a "autoremove=yes```

### add a user named gituser

```ansible all -m user -a "name=gituser" -b```

### remove a user named gituser

```ansible all -m user -a "remove=yes name=gituser" -b```

### display information about remote host

```ansible all -m setup```
