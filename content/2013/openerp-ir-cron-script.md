---
date: '2013-04-18'
title: Run OpenERP's ir.cron from command-line
category: English
tags: OpenERP, Python, CLI, cron, scheduler
---

Here is a simple Python script to trigger an `ir.cron` job from the
command-line system.

I created this to let my customer use his proprietary job scheduler to trigger
OpenERP tasks. It was tested on OpenERP 6.1.

```python
#!/usr/bin/python

import sys
import traceback
import xmlrpclib
from optparse import OptionParser
from datetime.datetime import now

parser = OptionParser()
parser.add_option("-d", "--db", dest="db_name", help="OpenERP database name", metavar="DB_NAME", default="openerp")
parser.add_option("-p", "--password", dest="password", help="OpenERP admin password", metavar="ADMIN_PASSWORD", default="admin")
parser.add_option("-n", "--name", dest="cron_name", help="OpenERP ir.cron object name", metavar="CRON_NAME")

(options, args) = parser.parse_args()

assert options.cron_name

# Query helpers
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
q = lambda * a: sock.execute(options.db_name, 1, options.password, *a)

try:
    ir_cron_ids = q('ir.cron', 'search', [('name', '=', options.cron_name)])
    if not ir_cron_ids:
        raise "No cron found in OpenERP."
    for ir_cron in q('ir.cron', 'read', ir_cron_ids, ['model', 'function', 'args']):
        print "%s, %s - (%s) %s %s%s" % (options.db_name, now().strftime('%Y-%m-%d %H:%M:%S'), ir_cron['id'], ir_cron['model'], ir_cron['function'], ir_cron['args'])
        q(ir_cron['model'], ir_cron['function'], *eval('tuple(%s)' % (ir_cron['args'] or '')))
except:
    traceback.print_exc(file=sys.stdout)
    sys.exit(8)

sys.exit()
```
