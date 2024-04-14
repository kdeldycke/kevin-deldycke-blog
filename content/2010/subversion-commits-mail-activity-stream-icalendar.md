---
date: '2010-06-16'
title: Subversion commits and mail activity stream in iCalendar
category: English
tags: code, commit, Git, GitHub, iCal, email, maildir, Python, Subversion
---

Last week I
[consolidated all my code]({filename}/2010/git-commit-history-reconstruction.md)
in [my GitHub repository](https://github.com/kdeldycke/scripts). I stumble upon
an old script I haven't published yet:
[`svn2ical.py`](https://github.com/kdeldycke/scripts/blob/master/svn2ical.py).

![]({attach}icalendar-subversion-commits.png)

This is a simple hack which get commit metadata out of a Subversion repository
and generate an iCalendar file containing all commits of a given author. I used
it back then to visualize my commit activity in a calendar. Nowadays this script
is quite useless as services like Open Hub
and [GitHub](https://github.com/kdeldycke) provides great timeline and activity
streams. But this script can still be useful for private repositories.

And in the same spirit of this script, I uncovered
[`maildir2ical.py`](https://github.com/kdeldycke/scripts/blob/master/maildir2ical.py),
a script that look in a maildir folder for mails sent by a particular author,
then generate an iCal file based on mail dates.
