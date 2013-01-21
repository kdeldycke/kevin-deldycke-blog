#!/usr/bin/python

##############################################################################
#
# Copyright (C) 2008 Kevin Deldycke <kev@coolcavemen.com>
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