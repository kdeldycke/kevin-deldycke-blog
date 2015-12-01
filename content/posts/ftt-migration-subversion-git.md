---
date: 2011-04-18 12:15:28
title: FTT Migration from Subversion to Git
category: English
tags: Feed Tracking Tool, Git, GitHub, migration, Subversion, Uperto

[Last month I released the Feed Tracking Tool project](http://kevin.deldycke.com/2011/03/feed-tracking-tool-released-open-source-license/) (aka FTT) [on GitHub](http://github.com/kdeldycke/feed-tracking-tool). I reconstructed the code history from old tarballs. In the mean time, my friend at Uperto managed to recover the original Subversion repository from very old backups. Here is how I migrated the old SVN repository to GitHub.

First, I started a local Subversion server with the repository my co-worker gave me:

    :::bash
    $ tar xvzf ./ftt-svn.tar.gz
    $ sed -i 's/# password-db = passwd/password-db = passwd/' ./ftt-svn/conf/svnserve.conf
    $ echo "kevin = kevin" >> ./ftt-svn/conf/passwd
    $ kill `ps -ef | grep svnserve | awk '{print $2}'`
    $ svnserve --daemon --listen-port 3690 --root ./ftt-svn

Then I created a local Git repository, using [my initialization routine](http://kevin.deldycke.com/2010/05/initialize-git-repositories/):

    :::bash
    $ rm -rf ./ftt-git
    $ mkdir ./ftt-git
    $ cd ./ftt-git
    $ git init
    $ git commit --allow-empty -m 'Initial commit'
    $ git tag "init"

The next step consist in importing the Subversion repository to Git:

    :::bash
    $ git svn init --no-metadata --username kevin svn://localhost:3690
    $ git svn fetch

Here I rebased the imported `git-svn` branch to the main branch:

    :::bash
    $ git rebase --onto git-svn master
    $ git rebase init master

At that point I don't need the remote `git-svn` branch so I removed it:

    :::bash
    $ git branch -r -D git-svn

To clean things up, let's remove all SVN metadatas and local commit backups:

    :::bash
    $ rm -rf ./.git/svn/
    $ rm -rf ./.git/refs/original/
    $ git reflog expire --all
    $ git gc --aggressive --prune

We can now proceed to alter the code history. In FTT we never created branches. I also plan to recreate tags by hand later. So I decided to remove all the `tags` and `branches` folders coming from Subversion:

    :::bash
    $ git filter-branch --force --prune-empty --tree-filter 'rm -rf ./tags*'     -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'rm -rf ./branches*' -- --all

Now let's move the `trunk` directory to the base of the repository. I didn't used the `--subdirectory-filter` parameter as FTT started its life without a proper "branches/tags/trunk" SVN structure:

    :::bash
    $ git filter-branch --force --prune-empty --tree-filter 'test -d ./trunk && cp -axv ./trunk/* ./ && rm -rf ./trunk || echo "No trunk folder found"' -- --all

Next is the Git command I used to fix commit authorship:

    :::bash
    $ git filter-branch --force --env-filter '
        if [ "$GIT_AUTHOR_NAME" = "kdeldycke" ]
          then
            export GIT_AUTHOR_NAME="Kevin Deldycke"
            export GIT_AUTHOR_EMAIL="kevin@deldycke.com"
        fi
        if [ "$GIT_AUTHOR_NAME" = "qdesert" ]
          then
            export GIT_AUTHOR_NAME="Quentin Desert"
            export GIT_AUTHOR_EMAIL="quentin.desert@uperto.com"
        fi
        ' -- --all

While exploring my own backups of the FTT project, I stumble upon a preliminary HTML mockup of the app. I decided to include it in the final repository, as the first commit, just after my `init` tag. Here how I did this, assuming the mockup sources were available in the `../mockup` directory:

    :::bash
    $ git branch mockup-injection init
    $ git checkout mockup-injection
    $ cp -axv ../mockup .
    $ git add --all
    $ git commit --all --date="2007-07-17 15:49" --author="Quentin Desert <quentin.desert@uperto.com>" -m "Commit the oldest mockup I can find."
    $ git rebase --onto mockup-injection init master
    $ git branch -D mockup-injection

The procedure above come from my "[Commit history reconstruction](http://kevin.deldycke.com/2010/06/git-commit-history-reconstruction/)" article.

Now I can tag by hand all FTT releases.

    :::bash
    $ git tag -f "0.4.1"  5f5cc2a36743f2c8d2088669e475ef09d8cec029
    $ git tag -f "0.5"    54a76e143f9f2efdec88d3181cbcfbfddda5f725
    $ git tag -f "0.6"    934447f185330903c389364bed94e994f6b280e6
    $ git tag -f '0.7'    ef87ab3287ba23655781565fd622345c942d9c49
    $ git tag -f "0.8"    cdcf2f459826019bbbc5874d6632392b07ea889b
    $ git tag -f "0.8.1"  f47a3f219eb918069efe701d082928cdb953f05f
    $ git tag -f "0.8.2"  2542754dd088d359ce96db8511e0a15588eb50ce
    $ git tag -f "0.8.3"  ea9455c0ed75cf504c1cc872d5e5946b578ae702
    $ git tag -f "0.9.0"  57a39879b3bcc61bd9560d7ac4e71cbfd0af22df
    $ git tag -f "0.9.1"  e483fd1a287fa86a8b12d088b78a319b0990e6ef
    $ git tag -f "0.10.0" ed77af77506836892be78044ae4ef15d07f18583

FTT was always developed as an internal app. As such the code and its history still contain lots of sensible informations. I deeply audited the code to identify the kind of data that we should absolutely not disclose to the outside world.

At the end of this code review, I just found references to our internal architecture (server's names and IP addresses), and some usernames and passwords. There was also some logs and temporary files. I cleaned them all with the following set of Git commands:

    :::bash
    $ git filter-branch --force --prune-empty --tree-filter 'find . -iname ".svn"        | xargs rm -rf' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -iname "*.log"       | xargs rm -rf' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -iname "*~"          | xargs rm -rf' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -iname "*.pid"       | xargs rm -rf' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -iname "*.ppid"      | xargs rm -rf' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -iname "ruby_sess.*" | xargs rm -rf' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -type f -exec sed -i "s/password: 1234567/password: *******/g"   "{}" \;' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -type f -exec sed -i "s/smtp\.server12\.com/smtp\.uperto\.com/g" "{}" \;' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -type f -exec sed -i "s/192\.168\.0\.2/12\.34\.56\.78/g"         "{}" \;' -- --all
    $ git filter-branch --force --prune-empty --tree-filter 'find . -type f -exec sed -i "s/user qdesert/user *******/g"             "{}" \;' -- --all

After all these modifications, I was pretty sure my code was ready to be published. But better safe than sorry, I spent a couple of minutes to do a second deep code review to check that I didn't missed anything. And to push the reviewing process even further, I offer a beer at the local bar for anyone finding sensible information in FTT's code base ! :)

The last things I did was to delete the old FTT's GitHub repository and recreate it. Then I fixed my first commit date, cleaned Git's local backup and pushed my carefully crafted repository to its new GitHub's home:

    :::bash
    $ export GIT_TMP_INIT_HASH=`git show-ref init | cut -d ' ' -f 1`
    $ git filter-branch --env-filter '
        if [ $GIT_COMMIT = $GIT_TMP_INIT_HASH ]
          then
            export GIT_AUTHOR_DATE="Thu, 01 Jan 1970 00:00:00 +0000"
            export GIT_COMMITTER_DATE="Thu, 01 Jan 1970 00:00:00 +0000"
        fi' -- --all
    $ unset GIT_TMP_INIT_HASH
    $ rm -rf ./.git/refs/original/
    $ git reflog expire --all
    $ git gc --aggressive --prune
    $ git remote add origin git@github.com:kdeldycke/feed-tracking-tool.git
    $ git push origin master --force --tags

