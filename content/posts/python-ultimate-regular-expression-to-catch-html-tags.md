---
date: 2008-07-08 00:24:26
title: Python ultimate regular expression to catch HTML tags
category: English
tags: HTML, programming, Python, Regular expression, BeautifoulSoup, lxml
---

!!! alert alert-warning "Disclaimer"
    This is a dirty hack!
    
    To parse HTML or XML, use a dedicated library like the good old:
    
    * [`BeautifoulSoup`](https://pypi.python.org/pypi/beautifulsoup4) 
    * [`lxml.html`](https://lxml.de/lxmlhtml.html)

1 year and 3 months ago I've came with a
[PHP regexp to parse HTML tag soup](https://kevin.deldycke.com/2007/03/ultimate-regular-expression-for-html-tag-parsing-with-php/).

Here is an improved version, in Python (my favorite language so far), that is
normally much prone to detect strange HTML tags. It also support attributes
without value so it's closer to the
[HTML specification](https://www.w3.org/TR/REC-html40/), but doesn't strictly
stick to it in order to catch [tag soup](https://en.wikipedia.org/wiki/Tag_soup)
and malformatted tags.

    :::python
    ultimate_regexp = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"

And here is it applied in a trivial example (in a python shell):

    :::pycon
    >>> import re
    >>>
    >>> content = """This is the <strong>content</strong> in which we want to
    <em>find</em> <a href="https://en.wikipedia.org/wiki/Html">HTML</a> tags."""
    >>>
    >>> ultimate_regexp = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
    >>>
    >>> for match in re.finditer(ultimate_regexp, content):
    ...   print repr(match.group())
    ...
    '<strong>'
    '</strong>'
    '<em>'
    '</em>'
    '<a href="https://en.wikipedia.org/wiki/Html">'
    '</a>'
    >>>
