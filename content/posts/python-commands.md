---
date: 2011-01-04 12:04:12
title: Python commands
category: English
tags: ascii, Computer programming, date, dateutil, development, distutils, encoding, PEP8, PyPi, PDB, Python, socket, unicode, URL, urllib2, HTTP, PyLint, Fabric, pip

  * Add a [Python's debugger](http://docs.python.org/library/pdb.html) break point:

        :::python
        import pdb; pdb.set_trace()

  * Replace accentuated characters by their ASCII equivalent in a unicode string:

        :::python
        import unicodedata
        unicodedata.normalize('NFKD', u"éèàçÇÉÈ²³¼ÀÁÂÃÄÅËÍÑÒÖÜÝåïš™").encode('ascii', 'ignore')

  * Lambda function to transform a string to a URL-friendly ID:

        :::python
        getSafeURL = lambda s: '-'.join([w for w in ''.join([c.isalnum() and c or '-' for c in s.lower()]).split('-') if w])
 
  Better: use [`awesome-slugify`](https://pypi.python.org/pypi/awesome-slugify) package.

  * Sort a list of dicts by dict-key ([source](http://code.pui.ch/2007/07/23/python-sort-a-list-of-dicts-by-dict-key/)):

        :::python
        import operator
        [dict(a=1, b=2, c=3), dict(a=2, b=2, c=2), dict(a=3, b=2, c=1)].sort(key=operator.itemgetter('c'))

  * Set `urllib2` timeout ([source](http://www.voidspace.org.uk/python/articles/urllib2.shtml)):

        :::python
        import socket
        socket.setdefaulttimeout(10)

  * Start a dumb HTTP server on port 8000 ([source](http://news.ycombinator.com/item?id=2042008)):

        :::bash
        $ python -m SimpleHTTPServer 8000

  * Use [autopep8](http://pypi.python.org/pypi/autopep8/) to apply PEP8's coding style on all Python files:

        :::bash
        $ find ./ -iname "*.py" -exec autopep8 --in-place "{}" \;

  * Delete all `.pyc` and `.pyo` files in the system:

        :::bash
        $ find / -name "*.py[co]" -delete
        

## Date and time

I personnaly recommend using the [`Arrow`](http://crsmithdev.com/arrow/) package. But if you can't, here are pure-python snippets:

  * Add a month to the current date:

        :::python
        import datetime
        import dateutil
        datetime.date.today() + dateutil.relativedelta(months=1)


## Data

  * [Pandas snippets](http://kevin.deldycke.com/2015/11/pandas-snippets/)


## Package management

  * Generate a binary distribution of the current package:

        :::bash
        $ python ./setup.py sdist

  * Register, generate and upload to [PyPi](http://pypi.python.org) the current package as a source package, an egg and a dumb binary:

        :::bash
        $ python ./setup.py register sdist bdist_egg bdist_dumb upload


## Configuration

I maintain a set of default configuration files in my [`dotfiles` repository](https://github.com/kdeldycke/dotfiles):

  * PDB: [`~/.pdbrc`](https://github.com/kdeldycke/dotfiles/blob/master/dotfiles-common/.pdbrc) & [`~/.pdbrc.py`](https://github.com/kdeldycke/dotfiles/blob/master/dotfiles-common/.pdbrc.py)
  * Pip: [`~/.pip/pip.conf`](https://github.com/kdeldycke/dotfiles/blob/master/dotfiles-common/.pip/pip.conf)
  * PyPi: [`~/.pypirc`](https://github.com/kdeldycke/dotfiles/blob/master/dotfiles-common/.pypirc)
  * PEP 8: [`~/.config/pep8`](https://github.com/kdeldycke/dotfiles/blob/master/dotfiles-common/.config/pep8)
  * PyLint: [`~/.pylintrc`](https://github.com/kdeldycke/dotfiles/blob/master/dotfiles-common/.pylintrc)
  * Fabric: [`~/.fabricrc`](https://github.com/kdeldycke/dotfiles/blob/master/dotfiles-common/.fabricrc)
