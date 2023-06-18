---
date: "2006-11-15"
title: CVS commands
category: English
tags: CLI, CVS, KDE, Linux
---

- Download to your machine the `kdetoys` module from the KDE CVS:

  ```shell-session
  $ cvs -d:pserver:anonymous@anoncvs.kde.org:/home/kde checkout kdetoys
  ```

- Get the 22/09/2005 version of the `kdetoys` module source code:

  ```shell-session
  $ cvs -d:pserver:anonymous@anoncvs.kde.org:/home/kde co -D '22 Sep 2005' kdetoys
  ```

- The `-D` option used above is sticky. Use the following command when you no longer want to keep the dated version:

  ```shell-session
  $ cvs up -A kdetoys
  ```
