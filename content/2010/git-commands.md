---
date: '2010-02-21'
title: Git commands
category: English
tags: CLI, Git, GitHub, Software engineering
---

- Get a clean local copy of [my GitHub repository](https://github.com/kdeldycke/scripts) with read & write access:

  ```shell-session
  $ git clone git@github.com:kdeldycke/scripts.git
  ```

- Switch to another branch:

  ```shell-session
  $ git checkout another_branch
  ```

- Set the current repository in the state it was at commit `1234567`:

  ```shell-session
  $ git checkout 1234567
  ```

- Get the current commit number:

  ```shell-session
  $ git rev-parse HEAD
  ```

- Get a sorted list of all commit IDs:

  ```shell-session
  $ git rev-list --all --pretty=oneline | cut -d ' ' -f 1 | sort
  ```

- Print a nice graph of your commits sorted by date:

  ```shell-session
  $ git log --graph --all --pretty=oneline --abbrev-commit --date-order
  ```

- Revert a particular commit:

  ```shell-session
  $ git revert 119ff8
  ```

- Destroy all your local changes and get back a sane repository:

  ```shell-session
  $ git reset --hard
  ```

- Send local repository modifications to remote one:

  ```shell-session
  $ git push origin
  ```

- Attach a tag to a given commit:

  ```shell-session
  $ git tag "1.2.3" 8fe2934d1552c97246836987f0ea08e10ba749ae
  ```

- Publish all tags to the remote repository:

  ```shell-session
  $ git push --tags
  ```

- Add a remote repository located on GitHub as a submodule in the `./folder/project-copy` folder:

  ```shell-session
  $ git submodule add https://github.com/my-id/project.git ./folder/project-copy
  ```

- While playing with backups of a local repository, you may encounter this error:

  ```text
  Cannot rewrite branch(es) with a dirty working directory.
  ```

  In this case, you can get back a clean repository by removing all the unstaged changes:

  ```shell-session
  $ git stash
  ```

Other resources:

- [Git tips and tricks](https://github.com/git-tips/tips#git-tips)
- [Awesome git addons](https://github.com/stevemao/awesome-git-addons)
- [My `.gitconfig` configuration file](https://github.com/kdeldycke/dotfiles/blob/main/dotfiles/.gitconfig)
