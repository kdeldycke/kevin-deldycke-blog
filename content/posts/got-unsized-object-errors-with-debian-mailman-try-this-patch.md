---
date: 2008-12-29 20:02:22
title: Got "unsized object" errors with Debian's Mailman ? Try this patch !
category: English
tags: bug, Debian, Debian Etch, hack, email, mailman, patch, Python
---

Last week I came across a showstopper bug on Mailman 2.1.9-7, the [current version of Mailman package distributed with Debian Etch](http://packages.debian.org/etch/mailman).

Here is the python traceback (from `/var/log/mailman/error` logfile) I get each time I've sent a mail to my brand new mailing-list:

    :::pytb
    Dec 20 01:20:04 2008 (14275) Uncaught runner exception: len() of unsized object
    Dec 20 01:20:04 2008 (14275) Traceback (most recent call last):
      File "/usr/lib/mailman/Mailman/Queue/Runner.py", line 112, in _oneloop
        self._onefile(msg, msgdata)
      File "/usr/lib/mailman/Mailman/Queue/Runner.py", line 170, in _onefile
        keepqueued = self._dispose(mlist, msg, msgdata)
      File "/usr/lib/mailman/Mailman/Queue/IncomingRunner.py", line 130, in _dispose
        more = self._dopipeline(mlist, msg, msgdata, pipeline)
      File "/usr/lib/mailman/Mailman/Queue/IncomingRunner.py", line 153, in _dopipeline
        sys.modules[modname].process(mlist, msg, msgdata)
      File "/usr/lib/mailman/Mailman/Handlers/ToDigest.py", line 81, in process
        mbox.AppendMessage(msg)
      File "/usr/lib/mailman/Mailman/Mailbox.py", line 69, in AppendMessage
        g.flatten(msg, unixfrom=True)
      File "/usr/lib/mailman/pythonlib/email/Generator.py", line 101, in flatten
        self._write(msg)
      File "/usr/lib/mailman/pythonlib/email/Generator.py", line 136, in _write
        self._write_headers(msg)
      File "/usr/lib/mailman/pythonlib/email/Generator.py", line 182, in _write_headers
        header_name=h, continuation_ws='\t').encode()
      File "/usr/lib/mailman/pythonlib/email/Header.py", line 412, in encode
        newchunks += self._split(s, charset, targetlen, splitchars)
      File "/usr/lib/mailman/pythonlib/email/Header.py", line 297, in _split
        elen = charset.encoded_header_len(encoded)
      File "/usr/lib/mailman/pythonlib/email/Charset.py", line 354, in encoded_header_len
        raise repr(s)
    TypeError: len() of unsized object

    Dec 20 01:20:04 2008 (14275) SHUNTING: 1229732404.1069181+dcd89a08bf7911dac2db804b76cd42d20564c71c

Here is the corresponding (anonymized) mail sent to the mailing list from a Gmail account:

    :::text
    Received: by 10.180.244.13 with HTTP; Fri, 19 Dec 2008 16:32:22 -0800 (PST)
    Message-ID: <1f7b086f0812192632x7427c0f7u2048609ddd50673@mail.gmail.com>
    Date: Sat, 20 Dec 2008 01:32:22 +0100
    From: "Kevin" <kevin@my-domain.com>
    To: my-ml@lists.my-domain.com
    Subject: sqdfqsdfqsfd
    MIME-Version: 1.0
    Content-Type: text/plain; charset=UTF-8
    Content-Transfer-Encoding: base64
    Content-Disposition: inline
    Delivered-To: kevin@my-domain.com

    LS0KS2V2LgogIOKAoiBiYW5kOiBodHRwOi8vY29vbGNhdmVtZW4uY29tCiAg4oCiIGJsb2c6IGh0
    dHA6Ly9rZXZpbi5kZWxkeWNrZS5jb20K

And now my hackish tale. Based on a quick look at Mailman's source code, I made an educated guess that this error is just a side effect of the wrong assumption that the `s` variable in the `Charset.encoded_header_len()` method is always a string. So I came up with the following evil patch to handle (gracefully, I hope) the case of `s` being `None`.

Here is the [resulting patch](/uploads/2008/mailman-219-7-charset-handling.patch) of my python-fu:

    :::diff
    --- /usr/lib/mailman/pythonlib/email/Charset.py.orig   2008-12-28 19:46:23.000000000 +0100
    +++ /usr/lib/mailman/pythonlib/email/Charset.py        2008-12-20 01:42:37.000000000 +0100
    @@ -351,6 +351,7 @@
                 lenqp = email.quopriMIME.header_quopri_len(s)
                 return min(lenb64, lenqp) + len(cset) + MISC_LEN
             else:
    +            return s is not None and len(str(s)) or 0
                 return len(s)

         def header_encode(self, s, convert=False):

And it do the trick ! Of course I can't guarantee that this patch is the way to definitely fix the bug. And it may corrupt data. So **use it only if you're as crazy as me** ! :D

But I know, I know... As a responsible and serious hacker (sigh), I should report this bug to the Debian or Mailman project. But I'm still not familiar with Dedian's way of reporting bugs (and to be honest, I feel lazy these days :p ). Maybe, one day...
