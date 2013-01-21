comments: true
date: 2010-02-26 14:18:17
layout: post
slug: mysql-commands
title: MySQL commands
wordpress_id: 1222
category: English
tags: CLI, Databases, MySQL, SQL

  * List all users in the current MySQL server:

        :::text
        mysql> SELECT User, Host FROM mysql.user;

  * Remove a user from the server:

        :::text
        mysql> DROP USER '<User>'@'<Host>';

  * Remove all binary logs:

        :::text
        mysql> RESET MASTER;

  * Delete all binary logs but keep a week worth of logs:

        :::console
        mysql --verbose --execute="PURGE BINARY LOGS BEFORE '`date +"%Y-%m-%d" -d last-week`';"

    And if you put this in a cron-tab, don't forget to escape percents:

        :::console
        mysql --verbose --execute="PURGE BINARY LOGS BEFORE '`date +\%Y-\%m-\%d -d last-week`';"

  * Check, auto-repair and optimize all databases:

        :::console
        mysqlcheck --auto-repair --optimize --all-databases

  * Export a database:

        :::console
        mysqldump -u my_user "my-database" > data.sql

  * Here is a `cron`-able command to restart a MySQL service if no process found active:

        :::console
        [ `ps axu | grep -v "grep" | grep --count "mysql"` -le 0 ] && /etc/init.d/mysql restart

  * Monitor the queries being run ([source](http://blog.urfix.com/25-%E2%80%93-sick-linux-commands/)):

        :::console
        watch -n 1 mysqladmin --user=XXXXX --password=XXXXX processlist

  * Get the list of default configuration parameters the server will use regardless of the values set in config files ([source](http://dev.mysql.com/doc/refman/5.1/en/server-system-variables.html)):

        :::console
        mysqld --no-defaults --verbose --help

  * Migrate all tables of all databases from MyISAM to InnoDB:

        :::console
        mysql --skip-column-names --silent --raw --execute="SELECT CONCAT(table_schema , '.', table_name) FROM INFORMATION_SCHEMA.tables WHERE table_type='BASE TABLE' AND engine='MyISAM';" | xargs -I '{}' mysql --verbose --execute="ALTER TABLE {} ENGINE=InnoDB;"

