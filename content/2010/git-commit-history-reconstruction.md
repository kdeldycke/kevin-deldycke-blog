---
date: '2010-06-09'
title: Commit history reconstruction with Git
category: English
tags: commit, Git, GitHub, history, Init, Software engineering
---

Here is something I wanted to do for 3 years. I wanted to migrate my code repository from this:

![]({attach}dumb-code-revision-control-system.png)

to a proper [revision control system](https://en.wikipedia.org/wiki/Revision_control), like Subversion. And I wanted to reconstruct the commit history with all the proper dates. That's something I can't do with SVN.

Then came Git. I knew that Git was powerful enough to let me manipulate the history (at my own risks). So I studied it during the last weeks until I found an acceptable way to do exactly what I had in mind. Here are my notes regarding this journey.

First, I need to get a local copy of my GitHub repository. That's the place where I want all my code to reside at the end of the process.

```shell-session
$ cd ~
$ git clone git@github.com:kdeldycke/kev-code.git
```

In gitg, my untouched repository looks like this:

![]({attach}git-repository-at-start.png)

Notice all the pre-existing code.

Let's create a `history-injection` branch from the `init` tag. The later is the root of my repository, as explained in my previous post on [how I initialize my Git repositories]({filename}/2010/initialize-git-repositories.md).

```shell-session
$ git branch history-injection init
```

Then switch to our brand new branch:

```shell-session
$ git checkout history-injection
```

We are now in a safe and contained environment in which we can do all our dirty stuff. Let's move the file we want to add in our repository:

```shell-session
$ cp ~/kev-code/website-backup-2006_04_30.py ~/kev-code/website-backup.py
```

Commit this new file locally, as usual, but with a commit date set in the past:

```shell-session
$ cd ~/kev-code
$ git add --all
$ git commit --all --date="2006-04-30 23:17" -m "First version of a script to backup several remote websites via FTP and make bzip2 archives."
```

I can repeat the last steps to reconstruct the commit history of my `website-backup.py` script:

```shell-session
$ cp ~/kev-code/website-backup-2006_10_29.py ~/kev-code/website-backup.py
$ git commit --all --date="2006-10-29 23:13" -m "Delete previous backups if nothing has changed."
$ cp ~/kev-code/website-backup-2006_11_01.py ~/kev-code/website-backup.py
$ git commit --all --date="2006-11-01 23:14" -m "Keep monthly bzip2 snapshots of backups and incremental backups of the last 32 days thanks to rdiff-backup."
$ (...)
```

At last, the `history-injection` branch contain all version of `website-backup.py`:

![]({attach}history-injection-branch.png)

Now I'll use the `rebase` directive to insert the `history-injection` branch back in the main line (aka `master`). This insertion will take place just after the `init` tag. This translates to the following Git command:

```shell-session
$ git rebase --preserve-merges --onto history-injection init master
```

The `--preserve-merges` option is really important here to not let Git takes too much initiatives. Without this option, all our branches between the `init` tag and the head of the `master` branch will be rebased. Believe me, that's not what we want.

I no longer need my temporary `history-injection` branch. Let's remove it:

```shell-session
$ git branch -D history-injection
```

Now you should have a unique and straight history line from `init` tag to `master` head. Like this:

![]({attach}rebased-history-injection-branch.png)

Commits appears to be ordered as they should but you may not be as lucky as me. In fact the recently merge commits are stuck at the "bottom" (just after the `init` tag, as we asked Git to do on rebase). And you may find you in a situation where commits of the whole master branch are not chronologically ordered.

Here is such an example. It happened when I tried to rebase the full history of my `system-backup.py` script:

![]({attach}system-backup-script-rebase.png)

I haven't found a way to tell Git how to rebase by following commit dates. I know that something can be done with a command like:

```shell-session
$ git rebase --interactive init
```

But I haven't succeeded yet. So I left these commits unsorted for now. I may write another blog post in the future if I find a way to cleanly sort them. In the mean time, If you have a solution, I'll be happy to ear that!

Finally, when we have something that looks good, we can push our changes to our remote GitHub repository:

```shell-session
$ git push origin
```

But Git will complain: changing already-pushed commits is bad. As I [explained several weeks ago]({filename}/2010/how-to-fix-bad-commit-authorship-git.md), it's dangerous but I don't care. I'm the only user of this repository. So let's bypass Git's wise warnings:

```shell-session
$ git push origin +master:master
```

Et voilà! By repeating these steps several times, I moved my code to GitHub, with a consistent and clean commit history.
