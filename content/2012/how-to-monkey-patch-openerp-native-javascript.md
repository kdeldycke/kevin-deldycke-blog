---
date: '2012-02-21'
title: How-to monkey-patch OpenERP's native Javascript
category: English
tags: javascript, monkeypatch, OpenERP, Web, xml, ERP
---

Here is a classic editable list in [OpenERP v6.0](https://www.openerp.com/node/607/2011/01):

![]({attach}editable-list.png)

It's a custom view I created this month [at work](https://www.smile.fr/Solutions/ERP) for one of our customer to let him select a list of products, then batch-print their labels on stickers.

The view above is produced by the following XML:

```xml
<?xml version="1.0" encoding="utf-8"?>
<openerp>
 <data>
  <!-- Multi product printing wizard -->
  <record id="label_wizard_product_form" model="ir.ui.view">
   <field name="name">
    label.wizard.product.form
   </field>
   <field name="model">
    label.wizard.product
   </field>
   <field name="type">
    form
   </field>
   <field name="arch" type="xml">
    <form string="Label Wizard">
     <field colspan="4" name="line_ids" nolabel="1"/>
     <group col="2" colspan="2">
      <button icon="gtk-ok" name="action_print" string="Print" type="object"/>
     </group>
    </form>
   </field>
  </record>
  <record id="label_wizard_product_line_tree" model="ir.ui.view">
   <field name="name">
    label.wizard.product.line.tree
   </field>
   <field name="model">
    label.wizard.product.line
   </field>
   <field name="type">
    tree
   </field>
   <field name="arch" type="xml">
    <tree editable="bottom" string="Items">
     <field name="product_template_id"/>
     <field name="size_id"/>
     <field name="main_color_id"/>
     <field name="product_id"/>
     <field name="quantity"/>
    </tree>
   </field>
  </record>
 </data>
</openerp>

```

If you start searching a product template with the first field, you'll get a pop-up similar to this one:

![]({attach}fixed-width-popup-list.png)

As you can see, these kind of pop-up inherits the width of their parent field, which hide the end of all lines if they are too long. It becomes difficult to distinguish the items when all found objects have the same long prefix.

Now I want to get rid of this behavior and let the pop-up menu take all the necessary width it needs to fully display its content.

My instinct told me that this default style could easily be overridden with some static CSS directives. But digging deeper into [OpenERP web client code](https://bazaar.launchpad.net/~openerp/openobject-client-web/6.0/files), I realized that the width is dynamically set by the `many2one` widget itself.

The code responsible for this behavior is located in the [`addons/openerp/static/javascript/m2o.js`](https://bazaar.launchpad.net/~openerp/openobject-client-web/6.0/view/head:/addons/openerp/static/javascript/m2o.js) file, in the [`ManyToOne.prototype.on_keydown`](https://bazaar.launchpad.net/~openerp/openobject-client-web/6.0/view/head:/addons/openerp/static/javascript/m2o.js#L267) method:

```javascript
ManyToOne.prototype.on_keydown = function(evt) {
    (...)
    jQuery('div.autoTextResults[id$="' + this.name + '"]').width(w)
        (...)
};
```

My goal is now to alter this default behavior, without touching the code in `m2o.js`.

And [thanks to Bryan Forbes' article](https://www.reigndropsfall.net/2010/06/15/monkey-patching/), I engineered a method to [monkey patch](https://wikipedia.org/wiki/Monkey_patch) the original `ManyToOne.prototype.on_keydown` Javascript method.

Here is the code I added in the XML view, just below the `line_ids` field:

```xml+js
<field name="line_ids" colspan="4" nolabel="1"/>
<html>
  <script type="text/javascript">
    $(document).ready(function(){
      (function(){
        var on_keydown_orig = ManyToOne.prototype.on_keydown;
        ManyToOne.prototype.on_keydown = function(evt) {
          var result = on_keydown_orig.call(this, evt);
          $(".autoTextResults").css('width', 'auto');
          return result;
        };
      })();
    });
  </script>
</html>
```

The result of this is a nice looking pop-up which doesn't break any vanilla Javascript of the OpenERP web client:

![]({attach}variable-width-popup-list.png)
