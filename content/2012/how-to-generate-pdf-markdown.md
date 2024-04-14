---
date: '2012-01-31'
title: How-to generate PDF from Markdown
category: English
tags: convertion, Gimli, GitHub, LaTeX, Linux, markdown, natty, pandoc, pdf, ruby, TeX, Ubuntu Natty Narwhal (11.04)
---

## Pandoc

The first tool you can use to convert a [Markdown](https://en.wikipedia.org/wiki/Markdown) file to PDF is [Pandoc](https://johnmacfarlane.net/pandoc/).

To install Pandoc and all its dependencies on my Ubuntu 11.04, I used the following command:

```shell-session
$ aptitude install pandoc texlive
```

Then I applied the PDF transformation on the [README.md](https://github.com/kdeldycke/openerp.buildout/blob/master/README.md) file from my [openerp.buildout GitHub project](https://github.com/kdeldycke/openerp.buildout):

```shell-session
$ wget https://raw.github.com/kdeldycke/openerp.buildout/master/README.md
$ pandoc README.md -o readme-pandoc.pdf
```

[The result]({attach}readme-pandoc.pdf) is good, but not perfect. For example code blocks with long lines don't break at the end of the page:

![]({attach}pandoc-non-wrapping-code-blocks.png)

While trying to solve this issue, I stumble upon another tool...

## Gimli

[Gimli](https://github.com/walle/gimli) is an utility that was explicitly written with GitHub in mind.

Gimli is written in Ruby, so let's install it the Ruby way:

```shell-session
$ aptitude install rubygems wkhtmltopdf
$ gem install gimli
```

Then we can convert our Markdown file to a PDF. The following will generate a README.pdf file in the current folder:

```shell-session
$ /var/lib/gems/1.8/bin/gimli -f ./README.md
```

The [resulting PDF]({attach}readme-gimli.pdf) is really close to how GitHub renders Markdown content on its website. And it solve the bad code block style of Pandoc:

![]({attach}gimli-wrapping-code-blocks.png)
