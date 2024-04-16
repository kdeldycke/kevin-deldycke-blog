---
date: '2015-09-28'
title: 'How-to reconcile metadata differences of a messed up pull-request '
category: English
tags: CLI, Git, GitHub, Linux, Babel, l10n, i18n, Python
---

I was browsing upcoming changes in [Babel
](https://github.com/python-babel/babel) today when I spotted a typo. For these
kind of tiny fixes I don't bother: I simply edit the file through GitHub UI and
let it forked the repository, name the branch and propose a [pull request
](https://github.com/python-babel/babel/pull/264) for me.

But now the [maintainer asked me
](https://github.com/python-babel/babel/pull/264#issuecomment-143711250) to
make my commit message more informative. Fair enough. This shouldn't take long.

So I fetched a local copy of my fork, made the edit and pushed it back:

```shell-session
$ git clone https://github.com/kdeldycke/babel.git
$ cd ./babel
$ git checkout patch-1
$ git rebase -i HEAD~10
$ git push --force
```

It's only after looking at the pull request in GitHub that I realized the last
ten commits were marked as new and different, while I expected only last one to
be featured as a change against `master`. In a word, I messed-up.

A closer inspection revealed that `rebase` seems to have introduced extra
`Committer` metadata. And my confidence that it would not made me force the
subsequent `push`.

It's now time to untangle this mess. I first tried to realign authorship
metadata on the last 10 commits ([665212
](https://github.com/python-babel/babel/commit/665212) being my PR's root, i.e.
the last untouched commit):

```shell-session
$ git filter-branch --force --env-filter '
    export GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME"
    export GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
' -- 665212..patch-1
```

Still, commit checksums did not returned to their original value. There must be
other metadata involved.

As I wasn't ready to waste time on doctoring each commit to find the
underlying differences, I simply rebased everything to master:

```shell-session
$ git rebase master
$ git pull
$ git rebase origin/master
$ git push --force
```

It did work and my PR was now clean and tidy.
