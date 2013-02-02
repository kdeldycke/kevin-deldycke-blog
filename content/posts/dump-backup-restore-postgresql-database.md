date: 2012-03-06 12:17:58
title: Dump, backup and restore a PostgreSQL database
category: English
tags: Backup, Dump, Linux, PostgreSQL, SQL, RDBMS

Between user rights, permissions, templates and encoding, believe me or not, but I had some troubles finding a consistent procedure to dump, backup and restore a [PostgreSQL](http://www.postgresql.org/) database. That's expected as I'm new to this RDBMS.

So here is the sequence of commands I use to dump a database from a server and copy it to another:

    :::bash
    postgres@source-server:~$ pg_dump my_db -v --format=c --file=./my_db_2011-11-23.dump
    postgres@source-server:~$ scp ./my_db_2011-11-23.dump postgres@dest-server:~/

Before importing the dump to a new database:

    :::bash
    postgres@dest-server:~$ createdb -E UTF8 -T template0 new_db
    postgres@dest-server:~$ pg_restore -U my_user -d new_db ./my_db_2011-11-23.dump
    postgres@dest-server:~$ psql --command "ALTER DATABASE new_db OWNER TO my_user;"

This hasn't failed me yet, and I'll update that post if it will.
