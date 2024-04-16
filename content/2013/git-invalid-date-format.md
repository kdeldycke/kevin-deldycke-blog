---
date: '2013-06-23'
title: 'Git fatal error: invalid date format: 0 +0000'
category: English
tags: Git, GitHub, maildir, python, code, datetime
---

[Moving `maildir-deduplicate.py` to its own repository]({filename}/2013/maildir-deduplicate-moved.md)
was tricky, as I wanted to keep the commit history.

[I followed my old notes from a previous article]({filename}/2011/moving-git-subtree-repository.md)
and started the migration process:

```shell-session
$ git clone git@github.com:kdeldycke/scripts.git
$ cd ./scripts
```

But I didn't went very far. As soon as I tried to remove all content but the
script from the revision tree, I stumble upon a puzzling error:

```shell-session
$ git filter-branch --prune-empty --tree-filter 'find ./ -maxdepth 1 -not -name "maildir-deduplicate.py" -and -not -path "./.git*" -and -not -path "./" -print -exec rm -rf "{}" \;' -- --all
Rewrite 8fe2934d1552c97246836987f0ea08e10ba749ae (1/174)fatal: invalid date format: 0 +0000
could not write rewritten commit
```

The bad commit the message refers to is the first one. It's a special commit I
create everytime I
[initialize a Git repository]({filename}/2010/initialize-git-repositories.md).

From the error message, I suspected a wrong date format. So I reset it:

```shell-session
$ export GIT_TMP_INIT_HASH=`git show-ref init | cut -d ' ' -f 1`
$ git filter-branch --env-filter '
    if [ $GIT_COMMIT = $GIT_TMP_INIT_HASH ]
        then
            export GIT_AUTHOR_DATE="Thu, 01 Jan 1970 00:00:00 +0000"
            export GIT_COMMITTER_DATE="Thu, 01 Jan 1970 00:00:00 +0000"
    fi' -- --all
$ unset GIT_TMP_INIT_HASH
```

Then I called my previous `git filter-branch` command but failed the same way.

I tried another date scheme:

```shell-session
$ export GIT_TMP_INIT_HASH=`git show-ref init | cut -d ' ' -f 1`
$ git filter-branch --env-filter '
    if [ $GIT_COMMIT = $GIT_TMP_INIT_HASH ]
        then
            export GIT_AUTHOR_DATE="1970-01-01 00:00:00 +0000"
            export GIT_COMMITTER_DATE="1970-01-01 00:00:00 +0000"
    fi' -- --all
$ unset GIT_TMP_INIT_HASH
```

Same error again.

Finally, the command below fixed this issue once and for all:

```shell-session
$ export GIT_TMP_INIT_HASH=`git show-ref init | cut -d ' ' -f 1`
$ git filter-branch --env-filter '
    if [ $GIT_COMMIT = $GIT_TMP_INIT_HASH ]
        then
            export GIT_AUTHOR_DATE="$(TZ=UTC date -d@100000000 -R)"
            export GIT_COMMITTER_DATE="$(TZ=UTC date -d@100000000 -R)"
    fi' -- --all
$ unset GIT_TMP_INIT_HASH
```

As you can see it sets the dates further in time (100000000 seconds after
epoch).

And you know why this works? Because recent version of
[Git don't allow dates with less than 9 digits](https://stackoverflow.com/a/5093714/487610).

That was not excepted, but it allowed me to proceed in my repository migration.
