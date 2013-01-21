comments: true
date: 2011-03-14 11:29:27
layout: post
slug: fixing-messed-up-encoding-mysql
title: Fixing messed-up encoding in MySQL
wordpress_id: 2994
category: English
tags: Character encoding, Databases, e107, Latin-1, MySQL, PHP, sed, SQL, unicode, UTF-8, Web

[Currently working](http://kevin.deldycke.com/2011/03/e107-importer-1-1/) on my [e107 Importer plugin](http://wordpress.org/extend/plugins/e107-importer/), I was confronted today with badly-encoded data coming from my databases.

e107 migrated to full UTF-8 [years ago](http://e107.org/comment.php?comment.news.735), but I must have messed the upgrade process at the time. That was my conclusion when I took a close look to my tables: all of them seems to be set to Latin-1 but contain UTF-8 data. Here are screenshots from [SQLBuddy](http://www.sqlbuddy.com) (a great light-weight MySQL manager) showing just that:
[![](http://kevin.deldycke.com/wp-content/uploads/2011/03/e107-latin1-encoded-mysql-tables-300x197.png)](http://kevin.deldycke.com/wp-content/uploads/2011/03/e107-latin1-encoded-mysql-tables.png)
[![](http://kevin.deldycke.com/wp-content/uploads/2011/03/utf8-encoded-data-in-latin1-tables-300x112.png)](http://kevin.deldycke.com/wp-content/uploads/2011/03/utf8-encoded-data-in-latin1-tables.png)

To fix this, I first tried to use the following command I [found on the web](http://www.commandlinefu.com/commands/view/1575/convert-all-mysql-tables-and-fields-to-utf8):


    :::console
    mysql --database=e107db -B -N -e "SHOW TABLES"  | awk '{print "ALTER TABLE", $1, "CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;"}' | mysql --database=e107db




But this doesn't work, as it not only change the encoding of the table, but also transcode the data inside the table.

Let's try something else. First, we'll export the database to a dump file, of which the encoding is forced to Latin-1:


    :::console
    mysqldump -a -c -e --no-create-db --add-drop-table --default-character-set=latin1 --databases 'e107db' > ./e107-data.sql




Now the trick is to change the `CHARSET` parameter of all `CREATE TABLE` directives to UTF-8:


    :::console
    sed -i 's/CHARSET=latin1/CHARSET=utf8/g' ./e107-data.sql




We'll also change the `NAMES` directive to force MySQL to handle imported data as UTF-8:


    :::console
    sed -i 's/SET NAMES latin1/SET NAMES utf8/g' ./e107-data.sql




Then we're free to import the result in a new UTF-8 database:


    :::console
    sed -i 's/USE `e107db`;/#USE `e107db`;/g' ./e107-data.sql
    mysql --execute="CREATE DATABASE e107db_new CHARACTER SET=utf8"
    mysql --database=e107db_new < ./e107-data.sql




And now, accentuated characters appears as they should in our database, meaning we've fixed all the mess ! :)

[![](http://kevin.deldycke.com/wp-content/uploads/2011/03/e107-utf8-encoded-mysql-tables-300x197.png)](http://kevin.deldycke.com/wp-content/uploads/2011/03/e107-utf8-encoded-mysql-tables.png)
[![](http://kevin.deldycke.com/wp-content/uploads/2011/03/fixed-utf8-data-in-tables-300x113.png)](http://kevin.deldycke.com/wp-content/uploads/2011/03/fixed-utf8-data-in-tables.png)

PS: I [found another alternative method](http://en.gentoo-wiki.com/wiki/Convert_latin1_to_UTF-8_in_MySQL#Alternative_Method) (look at the end of the linked page) which consists of temporarily handling `TEXT` fields as `BLOB`, to have MySQL treat them as binary content (thus skipping character transcoding). Haven't tested this but sounds tricky.
