---
date: 2012-10-02 12:37:23
title: Converting a bbPress Forum to a Mailbox Archive
category: English
tags: Backup, bbpress, convertion, Cool Cavemen, CSV, email, mailbox, mbox, migration, MySQL, SQL, PHP, Python, SQL, WordPress
---

In my band [Cool Cavemen](https://coolcavemen.com), before using a private mailing-list to discuss internal stuff, we were using a private bbPress forum. This forum is no longer used but it still contains tons of old, but useful content.

I've just finished to migrate this forum from [bbPress](https://bbpress.org/) to a [mailbox](https://en.wikipedia.org/wiki/Mbox) archive. Here is how I did it.

First, I simply opened a MySQL terminal on a local copy of our bbPress site:

    :::bash
    $ mysql -u root
    mysql> USE bbpress;

We have several forums there, we're only interested in the private one. Let's get its ID:

    :::console
    mysql> SELECT ID, post_title FROM wp_posts WHERE post_type = "forum";
    +-------+----------------+
    | ID    | post_title     |
    +-------+----------------+
    | 13884 | Private forum  |
    |  2891 | Public forum   |
    +-------+----------------+

For safety, check the number of topics and replies in our forum, to make sure we're on the right track:

    :::console
    mysql> SELECT COUNT(ID) FROM wp_posts WHERE post_type = "topic" AND post_parent = 13884;
    +-----------+
    | COUNT(ID) |
    +-----------+
    |       776 |
    +-----------+
    mysql> SELECT COUNT(ID) FROM wp_posts WHERE post_type = "reply" AND post_parent IN (SELECT ID FROM wp_posts WHERE post_type = "topic" AND post_parent = 13884);
    +-----------+
    | COUNT(ID) |
    +-----------+
    |     18104 |
    +-----------+

We can now export the content of topics to a CSV file (`/tmp/forum-topic-export.csv`) directly from a MySQL query:

    :::mysql
    SELECT p.ID AS msg_id, p.ID AS topic_id, u.display_name AS realname, u.user_email AS from, p.post_date_gmt AS date, p.post_title AS subject, p.post_content AS body
        INTO OUTFILE '/tmp/forum-topic-export.csv'
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        ESCAPED BY '\\'
        LINES TERMINATED BY '\r\n'
    FROM wp_posts AS p
    LEFT JOIN wp_users AS u ON p.post_author = u.ID
    WHERE p.post_type = "topic" AND p.post_parent = 13884;

Next, it is for replies to be exported (to `/tmp/forum-reply-export.csv`):

    :::mysql
    SELECT p.ID AS msg_id, p.post_parent AS topic_id, u.display_name AS realname, u.user_email AS from, p.post_date_gmt AS date, p.post_title AS subject, p.post_content AS body
        INTO OUTFILE '/tmp/forum-reply-export.csv'
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        ESCAPED BY '\\'
        LINES TERMINATED BY '\r\n'
    FROM wp_posts AS p
    LEFT JOIN wp_users AS u ON p.post_author = u.ID
    WHERE p.post_type = "reply" AND p.post_parent IN (
        SELECT ID
        FROM wp_posts
        WHERE post_type = "topic" AND post_parent = 13884
    );

I then wrote a [tiny Python script](https://github.com/kdeldycke/scripts/blob/master/bbpress-to-mailbox.py) to parse those CSV files and transform each forum post to an email. All these email are then consolidated in a single mailbox file.

Once this is done, it's easy to transfer these mails to any mail account using, for example, the [ImportExportTools plugin](https://addons.mozilla.org/thunderbird/addon/importexporttools/) for [Thunderbird](https://www.mozilla.org/thunderbird/).

Finally, once your confident enough (read: have lots of MySQL backups) that all your forum's threads were safely converted to mails, you're free to purge your bbPress databases of the content you just migrated:

    :::mysql
    DELETE
    FROM wp_posts
    WHERE post_parent IN (
        SELECT ID
        FROM wp_posts
        WHERE post_parent = 13884
    );
    DELETE
    FROM wp_posts
    WHERE post_parent = 13884;

