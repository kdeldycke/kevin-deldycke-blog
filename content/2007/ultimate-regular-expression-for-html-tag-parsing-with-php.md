---
date: '2007-03-23'
title: Ultimate Regular Expression for HTML tag parsing with PHP
category: English
tags: HTML, parsing, PHP, Regular expression
---

!!! alert alert-warning "Disclaimer"
    This is a dirty hack!

    To parse HTML or XML, use a dedicated library.

Tonight I found the ultimate
[regex](https://en.wikipedia.org/wiki/Regular_expression) to get HTML tags out of
a string. It was
[written a year ago by Phil Haack on his blog](https://haacked.com/archive/2005/04/22/Matching_HTML_With_Regex.aspx).
His regex is quite bullet-proof: it's able to parse HTML tags written on
multiple lines which contain any sort of attributes (with or without a value,
with single or double quotes).

Unfortunately his regular expression was designed for Microsoft .NET, so I've
spend some time to convert it to PHP. Here is the result:

```php
$regex = "/<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>/i";
```

And finally, my version based on the one above:

```php
$regex = "/<\/?\w+((\s+(\w|\w[\w-]*\w)(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>/i";
```

The latter include the following enhancement:

- accept hyphens as attribute's middle characters (
  [thanks Ged](https://kevin.deldycke.com/2007/ultimate-regular-expression-for-html-tag-parsing-with-php#comment-769310266))
