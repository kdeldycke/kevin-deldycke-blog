comments: true
date: 2008-08-22 00:42:05
layout: post
slug: how-to-e107-autogallery-to-zenphoto-migration
title: How-to: e107 autogallery to Zenphoto migration
wordpress_id: 310
category: English
tags: autogallery, e107, Linux, migration, MySQL, SQL, Python, Script, Snippet, SQL, Web, Zenphoto

These past few days I was working on the [Cool Cavemen's photo gallery](http://coolcavemen.com/photos) to move it to a shiny new one, powered by [Zenphoto](http://zenphoto.org). In this post I will roughly describe how I've done it, code and commands included.

The old gallery was based on [autogallery](http://sourceforge.net/projects/e107autogallery), a [e107](http://e107.org) plugin. We assume here that both e107 and Zenphoto are well configured and installed at the root of you web hosting space (`/www` in this case).

The first step is to copy the autogallery album structure, with all its content, to Zenphoto:

    :::bash
    $ cd /www
    $ cp -ax ./e107_plugins/autogallery/Gallery/* ./zenphoto/albums/

Then we delete all previews, thumbnails and XML metadatas, to keep in Zenphoto original assets only:

    :::bash
    $ find ./zenphoto/albums/ -iname "*.xml" | xargs rm -f
    $ find ./zenphoto/albums/ -iname "pv_*" | xargs rm -f
    $ find ./zenphoto/albums/ -iname "th_*" | xargs rm -f

By now, you should be able to play with your medias using Zenphoto's admin interface.

But if you're unlucky as I was, you will find a strange bug which break down drag'n'drop album sorting. The fix I found was to remove, in photo filenames, the numerical prefix (and the following dot) set by autogallery to define the sort order. This operation should be performed, _before_ the copy from autogallery to Zenphoto (= the first command in this post). By the way, if you know a one-liner to do this, please, please... share ! :)

To migrate comments, I have no automatic solution. I choose to do this manually, editing the database by hand. In my case it was the quickest way as I only had a dozen of comments to migrate.

And last but not least, if you care about measuring the popularity of your photos, you should consider migrating the view counter associated with each of your media. Don't worry, this time I wrote a script to take care of it automagically. It will generate a bunch of SQL statements you'll have to execute on your Zenphoto MySQL database. Here is my ["e107 autogallery to Zenphoto hit counter migration script"](http://kevin.deldycke.com/wp-content/uploads/2008/08/e107-autogallery-to-zenphoto-hit-counter-migration.py) (nice name isn't it ? ;) ) that do the job:

    :::python
    #!/usr/bin/python

    ##############################################################################
    #
    # Copyright (C) 2008 Kevin Deldycke <kevin@deldycke.com>
    #
    # This program is Free Software; you can redistribute it and/or
    # modify it under the terms of the GNU General Public License
    # as published by the Free Software Foundation; either version 2
    # of the License, or (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program; if not, write to the Free Software
    # Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
    #
    ##############################################################################

    """
      Last update: 2008 aug 21
    """

    ########### User config ###########

    AUTOGALLERY_ALBUM_PATH = "/www/e107_plugins/autogallery/Gallery"
    ZENPHOTO_ALBUM_PATH    = "/www/zenphoto/albums"
    ZENPHOTO_TABLE_PREFIX  = "zenphoto_"

    ######## End of user config #######

    import os, hashlib
    import xml.etree.ElementTree as ET

    # Calculate hash of a given file
    def getHash(path):
      # Calculate the hash from file raw data
      if not os.path.isfile(path):
        return None
      try:
        file_object = open(path, 'r')
        data = file_object.read()
      except:
        return None
      if not len(data):
        return None
      return hashlib.sha224(data).hexdigest()

    # Associate each autogallery photo having a hitcounter greater than 0 with its MD5 hash
    def populateHashTable(arg, dirname, names):
      global hash_table
      for name in names:
        file_path = os.path.join(dirname, name)
        # print "Get hit count for %s" % file_path
        # Check that the file as a positive hit counter associated with
        xml_file_path = "%s.xml" % file_path
        if not os.path.isfile(xml_file_path):
          continue
        try:
          tree = ET.parse(xml_file_path)
        except:
          continue
        node = tree.find("viewhits")
        if node is None:
          continue
        try:
          hits = int(node.text)
        except:
          continue
        if not hits > 0:
          continue
        # Update hash table with data we care about
        file_hash = getHash(file_path)
        if file_hash is None:
          continue
        hash_table[file_hash] = hits + hash_table.get(file_hash, 0)

    # Generate hitcount SQL request for each matching file
    def generateSQL(arg, dirname, names):
      global sql
      for name in names:
        file_path = os.path.join(dirname, name)
        # print "Search hitcounter matching file %s" % file_path
        file_hash = getHash(file_path)
        if file_hash is None:
          continue
        if file_hash in hash_table:
          sql += "UPDATE `%simages` SET `hitcounter`=`hitcounter`+%d WHERE `filename`=%r;\n" % (ZENPHOTO_TABLE_PREFIX, hash_table[file_hash], name)

    # Core of the script
    hash_table = {}
    sql        = ""
    # Normalize path
    source_path = os.path.abspath(AUTOGALLERY_ALBUM_PATH)
    dest_path   = os.path.abspath(ZENPHOTO_ALBUM_PATH)

    os.path.walk(source_path, populateHashTable, None)
    # print repr(hash_table)
    os.path.walk(dest_path, generateSQL, None)
    print sql

I think code and comments are self-explainatory. And do not forget to update constants at the top of the script to match your installation paths and database's tables prefix.

And finally, for your information, I tested all of this on following versions:

  * e107 0.7.11
  * autogallery 2.61
  * Zenphoto 1.2
  * Python 2.5.2
  * Linux server
