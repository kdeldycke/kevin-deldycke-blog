---
date: "2010-10-07"
title: Mercurial commands
category: English
tags: CLI, Mercurial
---

- Checkout a distant repository:

  ```shell-session
  $ hg clone https://bitbucket.org/mirror/django
  ```

- Commit all changes locally:

  ```shell-session
  $ hg commit -m "Here is my commit fixing bugs."
  ```

- Push local commits to the remote repository:

  ```shell-session
  $ hg push
  ```

- Apply latest changes of the remote repository to our local working copy:

  ```shell-session
  $ hg pull
  ```

- Align the current repository to a specific revision:

  ```shell-session
  $ hg update -r 502
  ```

- Restore all changes and files to the state they are in the distant repository:

  ```shell-session
  $ hg update -C
  ```

- My minimal `~/.hgrc` config file:

  ```ini
  [ui]
  username = Kevin Deldycke <kevin@deldycke.com>
  verbose = True

  [auth]
  # BitBucket creds
  bb.prefix = bitbucket.org
  bb.username = kdeldycke
  bb.password = XXXXXXXXXXX
  bb.schemes = https
  ```

- Display the last 5 commits:

  ```shell-session
  $ hg log --limit 5
  ```

- Display the local changes since last commit:

  ```shell-session
  $ hg diff
  ```

- Undo the last local commit:

  ```shell-session
  $ hg rollback
  ```

- Create a tag on a particular revision:

  ```shell-session
  $ hg tag -r 432 component-2.6.1
  ```

- Create a bundle file containing all changes committed locally:

  ```shell-session
  $ hg bundle fix-bug.bundle
  ```
