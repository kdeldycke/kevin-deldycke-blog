---
date: '2010-03-26'
title: OpenSSH commands
category: English
tags: CLI, Computer networking, find, Linux, openssh, proxy, rsync, scp, shell, SSH, tunnel, xargs
---

- Here is the syntax that makes `scp` support spaces ([source](https://rasterweb.net/raster/2005/01/27/scp-and-spaces/)):

  ```shell-session
  $ scp foo.com:"/home/fubar/some\ folder/file.txt" ./
  ```

- Copy a bunch of files to a remote server (or how to use `find` with `scp`):

  ```shell-session
  $ find /var/log/ -iname "*.log" -type f | xargs -i scp '{}' kevin@myserver:/media/backup/logs/
  ```

- Redirect local `8081` port to `proxy.company.com:8080` via a SSH tunnel passing through the `authorized-server.company.com` machine:

  ```shell-session
  $ ssh -T -N -C -L 8081:proxy.company.com:8080 kevin@authorized-server.company.com
  ```

- Use `rsync` over different SSH port ([source](https://lists.samba.org/archive/rsync/2001-November/000495.html)):

  ```shell-session
  $ rsync --progress -vrae 'ssh -p 8022' /home/user/docs/ bill@server:/home/user/docs/
  ```

Other resources:

- [SSH quoting](https://www.chiark.greenend.org.uk/~cjwatson/blog/ssh-quoting.html)
