date: 2015-11-18 16:32:12
title: How to solve SSL errors on pip install
category: English
tags: development, Python, socket, urllib3, HTTP, pip, requests, Apple, Mac OS X, Mac OS X El Capitan

Was trying to install [`alembic`](https://alembic.readthedocs.org) in a
[`virtualenv`](https://virtualenv.readthedocs.org) with [`pip`
](https://pip.readthedocs.org), on and OSX 10.11 machine:

    :::bash
    $ pip install alembic
    Collecting alembic
    (...)

Ended up with the following traceback:

    :::pytb
    Traceback (most recent call last):
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/basecommand.py", line 211, in main
        status = self.run(options, args)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/commands/install.py", line 305, in run
        wb.build(autobuilding=True)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/wheel.py", line 705, in build
        self.requirement_set.prepare_files(self.finder)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/req/req_set.py", line 334, in prepare_files
        functools.partial(self._prepare_file, finder))
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/req/req_set.py", line 321, in _walk_req_to_install
        more_reqs = handler(req_to_install)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/req/req_set.py", line 461, in _prepare_file
        req_to_install.populate_link(finder, self.upgrade)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/req/req_install.py", line 250, in populate_link
        self.link = finder.find_requirement(self, upgrade)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/index.py", line 486, in find_requirement
        all_versions = self._find_all_versions(req.name)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/index.py", line 444, in _find_all_versions
        for page in self._get_pages(url_locations, project_name):
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/index.py", line 641, in _get_pages
        page = self._get_page(location)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/index.py", line 818, in _get_page
        return HTMLPage.get_page(link, session=self.session)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/index.py", line 928, in get_page
        "Cache-Control": "max-age=600",
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/_vendor/requests/sessions.py", line 477, in get
        return self.request('GET', url, **kwargs)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/download.py", line 373, in request
        return super(PipSession, self).request(method, url, *args, **kwargs)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/_vendor/requests/sessions.py", line 465, in request
        resp = self.send(prep, **send_kwargs)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/_vendor/requests/sessions.py", line 573, in send
        r = adapter.send(request, **kwargs)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/_vendor/cachecontrol/adapter.py", line 46, in send
        resp = super(CacheControlAdapter, self).send(request, **kw)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/_vendor/requests/adapters.py", line 370, in send
        timeout=timeout
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/connectionpool.py", line 544, in urlopen
        body=body, headers=headers)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/connectionpool.py", line 344, in _make_request
        self._raise_timeout(err=e, url=url, timeout_value=conn.timeout)
      File "/Users/kev/venvs/test/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/connectionpool.py", line 314, in _raise_timeout
        if 'timed out' in str(err) or 'did not complete (read)' in str(err):  # Python 2.6
    TypeError: __str__ returned non-string (type Error)

Looking into the `connectionpool.py` file revealed the context as being some
sort of SSL-related validation.

By sheer luck I found the culprit in the name of the `cryptography` package.

After uninstalling it I was finally able to properly install `alembic`:

    :::bash
    $ pip uninstall cryptography
    Uninstalling cryptography-1.1:
    (...)
    Proceed (y/n)? y
      Successfully uninstalled cryptography-1.1

    $ pip install alembic
    Collecting alembic
    (...)
    Successfully installed alembic-0.8.3
