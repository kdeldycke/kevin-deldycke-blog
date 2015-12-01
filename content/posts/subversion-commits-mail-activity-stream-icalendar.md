---
date: 2010-06-16 21:53:46
title: Subversion commits and mail activity stream in iCalendar
category: English
tags: code, commit, Git, GitHub, iCal, email, maildir, Ohloh, Python, Script, Subversion

Last week I
[consolidated all my code](http://kevin.deldycke.com/2010/06/git-commit-history-reconstruction/)
in [my GitHub repository](http://github.com/kdeldycke/scripts). I stumble upon
an old script I haven't publicized yet:
  [`svn2ical.py`](http://github.com/kdeldycke/scripts/blob/master/svn2ical.py).

![](/uploads/2010/icalendar-subversion-commits.png)

This is a simple hack which get commit metadata out of a Subversion repository
and generate an iCalendar file containing all commits of a given author. I used
it back then to visualize in a calendar my commit activity. Nowadays this script
is quite useless as services like [Ohloh](http://www.ohloh.net/accounts/kevin)
and [GitHub](http://github.com/kdeldycke) provides great timeline and activity
streams. But this script can still be useful for private repositories.

And in the same spirit of this script, I uncovered
[`maildir2ical.py`](http://github.com/kdeldycke/scripts/blob/master/maildir2ical.py),
a script that look in a maildir folder for mails sent by a particular author,
then generate an iCal file based on mail dates.
