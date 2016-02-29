---
date: 2010-02-21 20:58:09
title: Git commands
category: English
tags: CLI, Git, GitHub, Software engineering
---

  * Get a clean local copy of [my GitHub repository](http://github.com/kdeldycke/scripts) with read & write access:

        :::bash
        $ git clone git@github.com:kdeldycke/scripts.git

  * Switch to another branch:

        :::bash
        $ git checkout another_branch

  * Set the current repository in the state it was at commit `1234567`:

        :::bash
        $ git checkout 1234567

  * Get the current commit number:

        :::bash
        $ git rev-parse HEAD

  * Get a sorted list of all commit IDs:

        :::bash
        $ git rev-list --all --pretty=oneline | cut -d ' ' -f 1 | sort

  * Print a nice graph of your commits sorted by date:

        :::bash
        $ git log --graph --all --pretty=oneline --abbrev-commit --date-order

  * Revert a particular commit:

        :::bash
        $ git revert 119ff8

  * Destroy all your local changes and get back a sane repository:

        :::bash
        $ git reset --hard

  * Send local repository modifications to remote one:

        :::bash
        $ git push origin

  * Attach a tag to a given commit:

        :::bash
        $ git tag "1.2.3" 8fe2934d1552c97246836987f0ea08e10ba749ae

  * Publish all tags to the remote repository:

        :::bash
        $ git push --tags

  * Add a remote repository located on GitHub as a submodule in the `./folder/project-copy` folder:

        :::bash
        $ git submodule add https://github.com/my-id/project.git ./folder/project-copy

  * While playing with backups of a local repository, you may encounter this error:

        :::text
        Cannot rewrite branch(es) with a dirty working directory.

    In this case, you can get back a clean repository by removing all the unstaged changes:

        :::bash
        $ git stash


Other resources:

  * [Git tips and tricks](https://github.com/git-tips/tips#git-tips)
  * [Awesome git addons](https://github.com/stevemao/awesome-git-addons)
  * [My `.gitconfig` configuration file](https://github.com/kdeldycke/dotfiles/blob/master/dotfiles-common/.gitconfig)
