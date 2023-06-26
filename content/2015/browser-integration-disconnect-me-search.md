---
date: "2015-12-01"
title: "Browser Integration of Disconnect.me search"
category: English
tags: security, Tor, privacy, StartPage, disconnect.me, search, browser, Google, Chrome
---

[Tor browser](https://www.torproject.org/projects/torbrowser.html.en) recently
[switched its default search
page](https://blog.disconnect.me/disconnect-is-the-new-default-search-provider-on-the-tor-browser/)
from [StartPage](https://startpage.com) to
[Disconnect.me](https://search.disconnect.me/). I followed suit and wanted to
change all my default browser search to the latter.

But if StartPage has [extensive
documentation](https://support.startpage.com/index.php?/Knowledgebase/Article/View/197/14/how-do-i-add-startpage-to-my-browser-generic-instructions-for-any-browser)
on adding default search to browser, I had a hard time finding details about
Disconnect.me.

Without further ado, here is the magic URL you're looking for:

    ```
    https://search.disconnect.me/searchTerms/search?ses=Google&query=%s
    ```

That's all you need to add Disconnect.me as your default search engine:

![Disconnect.me as default search engine in Google
Chrome](/uploads/2015/google-chrome-disconnect-me-default-search-engine.png)
