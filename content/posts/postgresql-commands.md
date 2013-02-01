date: 2011-10-25 12:40:47
slug: postgresql-commands
title: PostgreSQL commands
category: English
tags: CLI, database, Linux, PostgreSQL, SQL

  * Update the default configuration to allow direct authentication from the local machine:

        :::bash
        $ sed -i 's/^local\s\+all\s\+all\s\+ident/local all all trust/g' /etc/postgresql/8.4/main/pg_hba.conf

  * Same as above but for local IPv4 and IPv6 connexions:

        :::bash
        $ sed -i 's/^host\s\+all\s\+all\s\+\(.*\)\s\+md5/host all all \1 trust/g' /etc/postgresql/8.4/main/pg_hba.conf

  * List databases:

        :::bash
        $ psql --list -U kevin

  * Create a new `kevin_db` database with the `kevin` user:

        :::bash
        $ createdb -U kevin kevin_db

  * Remove the database we created above:

        :::bash
        $ dropdb kevin_db -U kevin

  * To connect to a particular database:

        :::bash
        $ psql -d database_id

  * Return the result of a query by aligning its row in a single line, separated by a space ([source](http://stackoverflow.com/a/1252191)):

        :::bash
        $ psql --tuples-only --no-align -d database_id -c "SELECT id FROM res_users;" | sed ':a;N;$!ba;s/\n/ /g'

  * Show us how a table of a specific database can be recreated:

        :::bash
        $ pg_dump my_database --schema-only --table=my_table

  * Dump a database in a compressed format:

        :::bash
        $ pg_dump my_database -v --format=c --file=/var/lib/postgresql/my_database-db-2011-12-19.dump

  * Restore a compressed dump:

        :::bash
        $ pg_restore -U my_user -d my_database /var/lib/postgresql/my_database-db-2011-12-19.dump

  * Import an SQL file to a database:

        :::bash
        $ psql --username kevin -d kevin_db < ./database_dump.sql

  * Search if `kevin` is a PostgreSQL user:

        :::bash
        $ sudo -u postgres psql --tuples-only --no-align --command "SELECT usename FROM pg_user;" | grep --quiet 'kevin' && echo 'User found !' || echo 'User not found !'

  * Set the owner of a database:

        :::postgresql
        ALTER DATABASE db_id OWNER TO user_id;

  * Set the owner of all tables from the `MY_DB_ID` database to `MY_DB_USER` ([source](http://stackoverflow.com/questions/1348126/modify-owner-on-all-tables-simultaneously-in-postgresql)):

        :::bash
        $ for tbl in `psql -qAt -c "SELECT tablename FROM pg_tables WHERE schemaname = 'public';" MY_DB_ID` ; do psql -c "ALTER TABLE $tbl OWNER TO MY_DB_USER" MY_DB_ID ; done

  * And to run the command above as the `postgres` user, while fixing sequences and views too, do:

        :::bash
        $ su - postgres <<-'.'
            DB_NAME=testdb
            DB_USER=openerp
            for tbl in `psql -qAt -c "SELECT tablename FROM pg_tables WHERE schemaname = 'public';" $DB_NAME` ; do psql -c "ALTER TABLE $tbl OWNER TO $DB_USER" $DB_NAME ; done
            for tbl in `psql -qAt -c "SELECT table_name FROM information_schema.views WHERE table_schema = 'public';" $DB_NAME` ; do psql -c "ALTER TABLE $tbl OWNER TO $DB_USER" $DB_NAME ; done
            for tbl in `psql -qAt -c "SELECT sequence_name FROM information_schema.sequences WHERE sequence_schema = 'public';" $DB_NAME` ; do psql -c "ALTER TABLE $tbl OWNER TO $DB_USER" $DB_NAME ; done
        .

  * Remove from a table all rows older than a month:

        :::bash
        $ sudo -u postgres psql -d database_id  --command "DELETE FROM smile_log WHERE log_date > current_date - interval '1 month';"

  * Extract an image that was saved in the database as base64 content, and save it on the file system:

        :::bash
        $ psql -d my_database -tc "COPY (SELECT decode(convert_from(image_bin, 'UTF-8'), 'base64') FROM res_partner WHERE id = 25) TO '/var/lib/postgresql/logo.png';"

  * Monitor queries being run in real time:

        :::bash
        $ watch -n 1 'sudo -u postgres psql --tuples-only --command "SELECT datname, procpid, date_trunc(\$\$second\$\$, age(current_timestamp, xact_start)), current_query FROM pg_stat_activity;"'

  * Disable all triggers of a table, excluding triggers that are used to implement foreign key constraints:

        :::bash
        $ ALTER TABLE table_id DISABLE TRIGGER ALL;

  * List all constraints of your database ([source](http://solaimurugan.blogspot.com/2010/10/list-out-all-forien-key-constraints.html)):

        :::postgresql
        SELECT tc.constraint_name,
        tc.constraint_type,
        tc.table_name,
        kcu.column_name,
        tc.is_deferrable,
        tc.initially_deferred,
        rc.match_option AS match_type,
        rc.update_rule AS on_update,
        rc.delete_rule AS on_delete,
        ccu.table_name AS references_table,
        ccu.column_name AS references_field
        FROM information_schema.table_constraints tc

        LEFT JOIN information_schema.key_column_usage kcu
        ON tc.constraint_catalog = kcu.constraint_catalog
        AND tc.constraint_schema = kcu.constraint_schema
        AND tc.constraint_name = kcu.constraint_name

        LEFT JOIN information_schema.referential_constraints rc
        ON tc.constraint_catalog = rc.constraint_catalog
        AND tc.constraint_schema = rc.constraint_schema
        AND tc.constraint_name = rc.constraint_name

        LEFT JOIN information_schema.constraint_column_usage ccu
        ON rc.unique_constraint_catalog = ccu.constraint_catalog
        AND rc.unique_constraint_schema = ccu.constraint_schema
        AND rc.unique_constraint_name = ccu.constraint_name

        WHERE lower(tc.constraint_type) in ('foreign key');

  * And finally, here is a list of [great monitoring one-liners](http://linuxhow-tos.blogspot.com/2011/03/monitor-postgresql-with-queries.html).

