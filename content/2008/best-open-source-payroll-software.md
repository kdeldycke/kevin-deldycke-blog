---
date: '2008-06-05'
title: I wrote the best Open-Source Payroll Software of the world!
category: English
tags: consulting, ERP, free software, open source, OpenERP, ERP5, OpenBravo, Neogia, Adempiere, Compiere
---

... at least [according Smile](https://www.smile.eu), a French consulting
company.

They studied [Open-Source
ERPs](https://en.wikipedia.org/wiki/Category:Free_ERP_software) in their latest white paper. It is [available for download
here](https://www.scribd.com/document/180544336/LB-Smile-ERP-pdf). And here is what they said about ERP5 at page 77:

> ERP5 va même jusqu'à gérer les paies alors qu'aucun autre ERP libre n'est
> allé aussi loin

Which roughly translates to:

> ERP5 even manage payroll, while any other free software ERP has gone as far

Hey wait. I wrote this module!

And here is their final evaluation (0 is the lowest, 5 the highest note) of all
payroll systems for each ERP (from page 88):

| ERP                                                           | Evaluation  |
| ------------------------------------------------------------- | ----------- |
| [TinyERP](https://en.wikipedia.org/wiki/Odoo#Company_history) | ★☆☆☆☆ (1/5) |
| [OpenBravo](https://en.wikipedia.org/wiki/Openbravo)          | ☆☆☆☆☆ (0/5) |
| [Neogia](https://sourceforge.net/projects/neogia/)            | ☆☆☆☆☆ (0/5) |
| [ERP5](https://en.wikipedia.org/wiki/ERP5)                    | ★★★★☆ (4/5) |
| [Adempiere](https://en.wikipedia.org/wiki/Adempiere)          | ☆☆☆☆☆ (0/5) |
| [Compiere GPL](https://en.wikipedia.org/wiki/Compiere)        | ☆☆☆☆☆ (0/5) |

As you can see I not only got the first place: I wiped out the competition.

Sorry for the shameless self-promotion, but I was so happy to get this
distinction after so many pain trying to transform laws into code that I
couldn't resist... :)

The payroll modules were one of my biggest [contribution as a core developer on
ERP5](https://openhub.net/p/erp5/contributors/18393197445279). It was
capable of [producing the
paysheets](https://web.archive.org/web/20110128111823/https://www.erp5.org/workspaces/project/erp5_payroll/erp5_pay_sheet_for_n/view)
of all Nexedi's employees. Here is an example:

![]({attach}erp5-final-paysheet.png)

These modules were so extensive that I wrote a detailed tutorial based on them.
As it was the only comprehensive documentation available on ERP5, my work
virtually became the [ERP5's bible for
developers](https://web.archive.org/web/20050924101245/https://www.erp5.org/sections/documentation/articles/erp5_developer_tutor3829/downloadFile/file/Tutorial-Kevin-en.pdf?nocache=1114902907.39)
for a while.

The [English translation is available for
download](https://web.archive.org/web/20050924101245/https://www.erp5.org/sections/documentation/articles/erp5_developer_tutor3829/downloadFile/file/Tutorial-Kevin-en.pdf?nocache=1114902907.39). The [original French version](https://web.archive.org/web/20091115172519/http://cps.erp5.org/sections/documentation/articles/erp5_developer_tutor/view), titled *Développez votre propre ERP grâce
aux Business Templates ERP5* has disappeared from the web.

This document was enough of a reference to be cited in a couple of academic papers from
2006 to 2009:

- [A comparison of Open Source ERP
  Systems](https://www.big.tuwien.ac.at/app/uploads/2016/10/Herzog_paper.pdf#page=77)

- [A Research on Corporate ERP Systems used for Supermarket Supply Chain
  Inventory Management in
  Turkey](https://www.slideshare.net/slideshow/embed_code/key/mHgCdv01fE9KsL?startSlide=13)

- [Open Source Enterprise Resource Planning
  Systems](https://behdasht.gov.ir/uploads/101_195_baresiye%20ERP%20haye%20matn%20baz.pdf)

- [Comparatif ERP5 /
  COMPIERE](https://web.archive.org/web/20101010002846/https://wiki.itin.fr/index.php/Comparatif_ERP5_/_COMPIERE_MT09_FR)

The irony is that after leaving the open-source ERP world in 2007, I was
recruited by Smile in 2011, the very same company which produced the original
white paper. My job? Working full on [OpenERP]({tag}openerp), the direct
competitor of ERP5.
