---
date: "2013-08-22"
title: "funky-storm.com source code released after 11 years"
tags: Funky Storm, PHP, MySQL, GitHub
---

[funky-storm.com](https://funky-storm.com) was the [first website I ever published](https://web.archive.org/web/20020515000000*/https://www.funkystorm.free.fr/) online, 11 years ago. Blogs were something new and there was virtually no mature open-source publishing platform, apart forums. Without any other options, I created my band's website from scratch.

I still have the source and I've just consolidated it in a [GitHub repository](https://github.com/kdeldycke/funky-storm) (thanks to my [history reconstruction process]({filename}/2010/git-commit-history-reconstruction.md)). Here is the detailed procedure:

```shell-session
$ rm -rf ./funky-storm
$ mkdir funky-storm
$ cd funky-storm
$ git init
$ for SNAPSHOT in 2002-09-29 2002-10-14 2003-01-07 2003-05-18 2004-02-28 2004-11-01
$ do
      cp -axv ../fs-code-snapshots/$SNAPSHOT/* .
      git add --all
      git commit --all --date="$SNAPSHOT 12:00:00" -m "$SNAPSHOT website code snapshot."
  done
$ git remote add origin git@github.com:kdeldycke/funky-storm.git
$ git push -u origin master
```

And if you're brave enough to [browse the code](https://github.com/kdeldycke/funky-storm), you'll see a huge mess of:

  * mixed PHP and HTML 4.0,
  * French variables and comments,
  * hard-coded parameters,
  * SQL injections,
  * flat files for databases,
  * inconsistent coding style,
  * Latin-1 strings,
  * table-based design,
  * and so on...

Digging deeper, I even found an old photo of me from my prime years:

![](https://raw.github.com/kdeldycke/funky-storm/master/data/webmaster.jpg)

This project was horrible from a software engineering point of view. And that's normal: it was part of my learning process. Hence the nostalgia.

The lack of code quality didn't prevent the website to do its job. Quite the contrary: we were the only band of our area with such an online presence. And before the coming of MySpace, that was enough to differentiate us from the crowd of ephemeral bands of the local scene.

But that's another story, which you can reconstruct by browsing (in French) the archives on [the new funky-storm.com](https://funky-storm.com)...
