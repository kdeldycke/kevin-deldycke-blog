comments: true
date: 2012-09-11 12:33:09
layout: post
slug: merging-git-outdated-subversion-fork
title: Merging back Git changes to an outdated Subversion fork
wordpress_id: 5083
category: English
tags: Git, GitHub, merge, OpenERP, Subversion

When working on an OpenERP project for a customer, we (sadly too frequently) have to keep in its private SVN repository a local copy of a module. I feel quite dirty when doing so but I have to admit it's a pragmatic approach. Especially when you have to quickly add loads of customizations on a tight schedule.

Months later, the tainted copy residing in SVN starts rotting, stucked with its customizations in an old version of the module. Meanwhile, the original module was updated at a fast pace and kept all its freshness and purity. It's time to reconcile the two versions and backport commits from Git to Subversion. The graph below sums up the situation:

![](/static/uploads/2012/09/git-svn-parallel-branches.png)

The arrow at the bottom between Git and Subversion is what we have done when we decided to copy the module in the customer's project repository. The top arrow is what we want to do.

The module we forked is the [matrix widget for OpenERP](https://github.com/Smile-SA/smile_openerp_matrix_widget). The copy happened at commit `8f189e44a3` and landed in SVN in revision `301`. That's our bottom arrow from the illustration.

Since then, the matrix module evolved a lot. It is now in Git at commit `b2810f0024`. We want to merge back [these changes](https://github.com/Smile-SA/smile_openerp_matrix_widget/compare/8f189e44a3...b2810f0024) to Subversion (currently at revision `501`).

Let's start by downloading a copy of the original module:

    :::bash
    $ git clone git@github.com:Smile-SA/smile_openerp_matrix_widget.git
    $ cd smile_openerp_matrix_widget

Now we'll import in a Git branch all customizations made in the copy living in SVN:

    :::bash
    $ git svn clone --no-metadata -r301:HEAD --username kevin svn://svn.company.com:3690/customer-project/trunk .
    $ git branch svn-trunk-copy git-svn
    $ git checkout svn-trunk-copy

At that point we don’t need the remote `git-svn` branch:

    :::bash
    $ git branch -r -D git-svn

As usual, the SVN repository is a mess and contain numerous stuff unrelated to our original matrix module. The only folders I want to keep, corresponding to the original Git repository, are located in:

  * `./addons-web/smile_matrix_widget/`
  * `./addons-server/smile_matrix_field/`

Let's remove all other content:

    :::bash
    $ git filter-branch --force --prune-empty --tree-filter 'find ./ -not -ipath "*_matrix_*" -and -not -path "./addons-web" -and -not -path "./addons-server" -and -not -path "./.git*" -and -not -path "./" | xargs rm -rf' --

I'll then move back these folders at the root of the SVN branch, to replicate the layout of the original Git repository:

    :::bash
    $ git filter-branch --force --prune-empty --tree-filter 'test -d ./addons-web && cp -axv ./addons-web/* ./ && rm -rf ./addons-web || echo "No ./addons-web folder found"' --
    $ git filter-branch --force --prune-empty --tree-filter 'test -d ./addons-server && cp -axv ./addons-server/* ./ && rm -rf ./addons-server || echo "No ./addons-server folder found"' --

Finally we remove unwanted Git metadata:

    :::bash
    $ rm -rf ./.git/svn/
    $ rm -rf ./.git/refs/original/
    $ git reflog expire --all
    $ git gc --aggressive --prune

If you're lost in this cleaning step, please have look at a previous article in which I explain [how I re-arranged a messy Subversion repository into a clean Git project](http://kevin.deldycke.com/2011/08/how-open-source-an-internal-corporate-project-webping/).

Now that we have a good looking SVN branch similar to our Git's, we can proceed to the merging itself:

    :::bash
    $ git branch svn-fork-point 8f189e44a3
    $ git rebase svn-fork-point
    $ git checkout svn-trunk-copy
    $ git merge master
    Auto-merging smile_matrix_widget/widgets/templates/matrix.mako
    CONFLICT (content): Merge conflict in smile_matrix_widget/widgets/templates/matrix.mako
    Auto-merging smile_matrix_widget/static/javascript/matrix.js
    CONFLICT (content): Merge conflict in smile_matrix_widget/static/javascript/matrix.js
    Auto-merging smile_matrix_field/matrix_field.py
    CONFLICT (content): Merge conflict in smile_matrix_field/matrix_field.py
    Automatic merge failed; fix conflicts and then commit the result.

The merged result is sitting on the `svn-trunk-copy` branch. Git made all the hard work. All you have to do is resolve tiny conflicts by hand.

Then commit back the result to your Subversion repository, in the right location:

    :::bash
    $ cd ..
    $ svn co svn://svn.company.com:3690/customer-project/trunk
    $ cp -axv ../smile_openerp_matrix_widget/smile_matrix_widget ./trunk/addons-web/
    $ cp -axv ../smile_openerp_matrix_widget/smile_matrix_field ./trunk/addons-server/
    $ svn commit -m "Merge back all changes from commit 8f189e44a3:b2810f0024 of the original smile_openerp_matrix_widget Git repository." ./trunk

