---
date: 2008-06-05 20:35:58
title: I wrote the best Open-Source Payroll Software of the world!
category: English
tags: consulting, ERP, free software, open source, OpenERP, ERP5, OpenBravo, Neogia, Adempiere, Compiere
---

... at least [according Smile](http://www.smile.fr), a French consulting
company. In their latest white paper ([available for download
here](http://www.smile.fr/Livres-blancs/ERP-et-decisionnel/ERP-open-source)),
they've studied [Open-Source
ERPs](http://en.wikipedia.org/wiki/Category:Free_ERP_software).

Here is what they said about ERP5 in page 87:

> ERP5 va même jusqu'à gérer les paies alors qu'aucun autre ERP libre n'est
allé aussi loin

Which roughly translates to:

> ERP5 even manage payroll, while any other free software ERP has gone as far

Hey wait. I wrote this module!

And here is their final evaluation (0 is the lowest, 5 the highest note) of all
payroll systems for each ERP (from page 88):

ERP | Evaluation
--- | ---
TinyERP | <i class="icon-star"></i>
OpenBravo | --
Neogia | --
ERP5 | <i class="icon-star"></i> <i class="icon-star"></i> <i class="icon-star"></i> <i class="icon-star"></i>
Adempiere | --
Compiere GPL | --

As you can see I not only got the first place: I wiped out the competition.

Sorry for the shameless self-promotion, but I was so happy to get this
distinction after so many pain trying to transform laws into code that I
couldn't resist... :)

The payroll modules were one of my biggest [contribution as a core developer on
ERP5](https://www.openhub.net/p/erp5/contributors/18391049963153). It was
capable of [producing the
paysheets](http://web.archive.org/web/20110128111823/http://www.erp5.org/workspaces/project/erp5_payroll/erp5_pay_sheet_for_n/view)
of all Nexedi's employees. Here is an example:

![](/uploads/2008/erp5-final-paysheet.png)

These modules were so extensive that I wrote a detailed tutorial based on them.
As it was the only comprehensive documentation available on ERP5, my work
virtually became the [ERP5's bible for
developers](http://web.archive.org/web/20050924101245/http://www.erp5.org/sections/documentation/articles/erp5_developer_tutor3829/downloadFile/file/Tutorial-Kevin-en.pdf?nocache=1114902907.39)
for a while.

The [English translation is available for
download](http://web.archive.org/web/20050924101245/http://www.erp5.org/sections/documentation/articles/erp5_developer_tutor3829/downloadFile/file/Tutorial-Kevin-en.pdf?nocache=1114902907.39),
while the original French version (titled *Développez votre propre ERP grâce
aux Business Templates ERP5*) has disappeared from the web.

This document had enough influence to be cited in four academic papers from
2006 to 2009:

  * [A comparison of Open Source ERP
  Systems](http://www.big.tuwien.ac.at/system/theses/20/papers.pdf)

  * [A Research on Corporate ERP Systems used for Supermarket Supply Chain
  Inventory Management in
  Turkey](http://www.slideshare.net/Agcristi/a-research-on-corporate-enterprise-resource-planning-erp)

  * [Open Source Enterprise Resource Planning
  Systems](http://behdasht.gov.ir/uploads/101_195_baresiye%20ERP%20haye%20matn%20baz.pdf)

  * [Comparatif ERP5 /
  COMPIERE](https://web.archive.org/web/20101010002846/http://wiki.itin.fr/index.php/Comparatif_ERP5_/_COMPIERE_MT09_FR)

The irony is that after leaving the open-source ERP world in 2007, I was
recruited by Smile in 2011, the very same company which produced the original
white paper. My job? Working full on [OpenERP]({tag}openerp), the direct
competitor of ERP5.
