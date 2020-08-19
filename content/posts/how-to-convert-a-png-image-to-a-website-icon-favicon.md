---
date: 2006-09-15 23:19:36
title: How to Convert a Png image to a Website Icon (favicon)
category: English
tags: CLI, Linux, Theme, Web
---

I know how to convert a [bitmap image](https://en.wikipedia.org/wiki/Windows_bitmap) to a website icon, thanks to the following one-line linux command:

    ```shell-session
    $ bmptoppm favicon.bmp | ppmtowinicon -output favicon.ico
    ```

This will convert the `favicon.bmp` file to `favicon.ico`.

Today I needed to do the same with a [Png file](https://en.wikipedia.org/wiki/Png) as input. After some tests, I found the corresponding command:

    ```shell-session
    $ pngtopnm -mix favicon.png | ppmtowinicon -output favicon.ico
    ```

This work well, but if the original `.png` file has an [alpha channel](https://en.wikipedia.org/wiki/Alpha_channel), it will be replaced by a white background.

To override this default behaviour, add the `background` option to `pngtopnm`. For example, if you want a blue background, the command to use is the following:

    ```shell-session
    $ pngtopnm -background=rgb:00/00/ff favicon.png | ppmtowinicon -output favicon.ico
    ```

In here, the `00/00/ff` parameter is the hexadecimal conversion of RGB encoding of the blue color.

By the way, if you need more informations about website icons, I advise you to take a look at the [favicon wikipedia article](https://en.wikipedia.org/wiki/Favicon). Here you will find useful tips about the conventions to apply in order to have a favicon supported by most (if not all) major browsers.
