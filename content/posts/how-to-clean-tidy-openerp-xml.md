date: 2012-12-18 12:30:05
slug: how-to-clean-tidy-openerp-xml
title: How-to clean and tidy up OpenERP's XML
category: English
tags: CLI, lint, Linux, OpenERP, xml, XSLT, ERP

Based on internal metrics, half of the OpenERP custom code I produce for my customers is Python. The other half is XML (_sigh_).

If Python is well-equiped to enforce coding styles (thanks to [pep8](http://pypi.python.org/pypi/pep8), [pyflakes](http://pypi.python.org/pypi/pyflakes), [pylint](http://pypi.python.org/pypi/pylint) and [the](http://pypi.python.org/pypi/autopep8) [likes](http://pypi.python.org/pypi/flake8)), it's another story for XML. After some investigations and experiments, here is the best way I found to automate the cleaning of huge quantities of XML content.

First, we have to install some command-line utilities:

    :::bash
    $ aptitude install libxml2-utils xsltproc

Override the default XML indention from 2 spaces to 4, before forcing the cleaning of each XML file found from our current folder:

    :::bash
    $ export XMLLINT_INDENT="    "
    $ find . -iname "*.xml" -exec xmllint --format --output "{}" "{}" \;

Now we have a set of normalized XML content.

Create an empty XSLT file named `tidy.xslt` and copy the following content in it:

    :::xslt
    <?xml version="1.0"?>
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

      <!-- Produce an exact copy of the original XML content -->
      <xsl:template match="@*|node()">
        <xsl:copy>
          <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
      </xsl:template>

      <!-- Insert blank lines between each child element of data tags -->
      <xsl:template match="data">
        <xsl:copy>
          <xsl:apply-templates select="@*"/>
          <xsl:text>
          </xsl:text>
          <xsl:apply-templates select="node()"/>
        </xsl:copy>
      </xsl:template>
      <xsl:template match="data/*">
        <xsl:copy>
          <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
        <xsl:text>
        </xsl:text>
      </xsl:template>

    </xsl:stylesheet>

The XSLT file above will separate with a blank line all children of all `data` tags. If this particular example is designed for OpenERP's XML, you can update the second and third `xsl:template` block to produce files fitting your taste and style.

Finally, you can apply our XSLT to all our local XML files:

    :::bash
    $ find . -iname "*.xml" -exec xsltproc --output "{}" ./tidy.xslt "{}" \;

