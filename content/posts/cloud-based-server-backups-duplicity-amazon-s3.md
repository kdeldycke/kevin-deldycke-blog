date: 2011-09-13 12:35:33
slug: cloud-based-server-backups-duplicity-amazon-s3
title: Cloud-based Server Backups with Duplicity and Amazon S3
category: English
tags: Amazon S3, AWS, Backup, cloud-computing, cron, Debian, duplicity, Linux, MySQL, SQL, shell, Debian Squeeze, storage

For years I was backing up my server with [`website-backup.py`](http://github.com/kdeldycke/scripts/blob/master/website-backup.py), a custom script I wrote to manage data mirroring, do incremental backups and monthly snapshots based on [`rdiff-backup`](http://www.nongnu.org/rdiff-backup/), `rsync`, `tar` and `bzip2`. All these data were pushed to a storage server hosted at home.

I've just replaced my script with [duplicity](http://duplicity.nongnu.org), a tool written by the same author of `rdiff-backup`. And [Amazon S3 cloud storage](http://aws.amazon.com/s3/) replaced my home server. Here is how I did it.

First, we need to create an account on [Amazon AWS](http://aws.amazon.com). This is easy and fast. My account was activated in minutes.

Now that you have access to Amazon's cloud, let's create a bucket on S3. I used the reversed domain name of the server, which give me a bucket name like `com.example.server.backup`. With this naming scheme, I can identify the purpose of the bucket by its label only.

Duplicity can use the [cheaper RRS storage](http://aws.amazon.com/about-aws/whats-new/2010/05/19/announcing-amazon-s3-reduced-redundancy-storage/), but you need at least version 0.6.09. Having a Debian Squeeze, the only way to get a recent version is to install it from the backports:

    :::bash
    $ apt-get -t squeeze-backports install duplicity python-boto

Then I created a simple symmetric key with GPG:

    :::bash
    $ gpg --gen-key

You absolutely need to provide a passphrase, else Duplicity will refuse to run.

Now update the script below with the GPG key passphrase and your AWS credentials:

    :::bash
    # Do not let this script run more than once
    [ `ps axu | grep -v "grep" | grep --count "duplicity"` -gt 0 ] && exit 1

    # Set some environment variables required by duplicity
    export PASSPHRASE=XXXXXXXXXX
    export AWS_ACCESS_KEY_ID=XXXXXXXXXX
    export AWS_SECRET_ACCESS_KEY=XXXXXXXXXX

    # ~/.cache/duplicity/ should be excluded, as explained in http://comments.gmane.org/gmane.comp.sysutils.backup.duplicity.general/4449
    PARAMS='--exclude-device-files --exclude-other-filesystems --exclude **/.cache/** --exclude **/.thumbnails/** --exclude /mnt/ --exclude /tmp/ --exclude /dev/ --exclude /sys/ --exclude /proc/ --exclude /media/ --exclude /var/run/ --volsize 10 --s3-use-rrs --asynchronous-upload -vinfo'
    DEST='s3+http://com.example.server.backup'

    # Export MySQL databases
    mysqldump --user=root --opt --all-databases > /home/kevin/mysql-backup.sql

    # Do the backup
    duplicity $PARAMS --full-if-older-than 1M / $DEST

    # Clean things up
    duplicity remove-older-than 1Y --force --extra-clean $PARAMS $DEST
    duplicity cleanup --force $PARAMS $DEST

    # Remove temporary environment variables
    unset PASSPHRASE
    unset AWS_ACCESS_KEY_ID
    unset AWS_SECRET_ACCESS_KEY

Before running duplicity, the script will dump all MySQL databases to a plain-text file. Then the first duplicity call will do the backup itself, and the second call will remove all backup older than a year.

I saved the script above in `/home/kevin/s3-backup.sh` and `cron`-ed it:

    :::bash
    $ chmod 755 /home/kevin/s3-backup.sh
    $ echo "
    # Backup everything to an Amazon S3 storage
    0 1 * * * root /home/kevin/s3-backup.sh
    " > /etc/cron.d/s3-backup

I can now sleep better knowing all the work I do on my server will not be lost in case of a catastrophic event. Amazon S3 is today a no-brainer for server backups: your data will be secured and available. And for small quantity of data (like the 10 Go of my server), it's incredibly cheap. Especially if you compare it to the cost of maintaining a storage server at home.

This solution is so good and obvious, that I don't know why I haven't implemented it earlier... :)
