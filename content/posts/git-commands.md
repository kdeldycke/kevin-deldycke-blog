comments: true
date: 2010-02-21 20:58:09
layout: post
slug: git-commands
title: Git commands
wordpress_id: 1130
category: English
tags: CLI, Git, GitHub, Project management software, Software engineering, Version control




  * Get a clean local copy of [my GitHub repository](http://github.com/kdeldycke/scripts) with read & write access:


        :::console
        git clone git@github.com:kdeldycke/scripts.git







  * Switch to another branch:


        :::console
        git checkout another_branch







  * Set the current repository in the state it was at commit `1234567`:


        :::console
        git checkout 1234567







  * Get the current commit number:


        :::console
        git rev-parse HEAD







  * Get a sorted list of all commit IDs:


        :::console
        git rev-list --all --pretty=oneline | cut -d ' ' -f 1 | sort







  * Print a nice graph of your commits sorted by date:


        :::console
        git log --graph --all --pretty=oneline --abbrev-commit --date-order







  * Destroy all your local changes and get back a sane repository:


        :::console
        git reset --hard







  * Send local repository modifications to remote one:


        :::console
        git push origin







  * Attach a tag to a given commit:


        :::console
        git tag "1.2.3" 8fe2934d1552c97246836987f0ea08e10ba749ae







  * Publish all tags to the remote repository:


        :::console
        git push --tags







  * Add a remote repository located on GitHub as a submodule in the `./folder/project-copy` folder:


        :::console
        git submodule add https://github.com/my-id/project.git ./folder/project-copy







  * While playing with backups of a local repository, you may encounter this error:


        :::text
        Cannot rewrite branch(es) with a dirty working directory.



  In this case, you can get back a clean repository by removing all the unstaged changes:


        :::console
        git stash







