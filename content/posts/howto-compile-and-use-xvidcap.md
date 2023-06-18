---
date: "2005-06-27"
title: "How-to Compile and Use xvidcap"
category: English
tags: CLI, Linux, Mandriva, mencoder, mplayer, Video, xvidcap
---

## Compile gvidcap!

Get the last stable source code archive on [xvidcap Sourceforge project page](https://sourceforge.net/projects/xvidcap) or download it from the [CVS](https://cvs.sourceforge.net/viewcvs.py/xvidcap):

    ```shell-session
    $ cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/xvidcap co -P xvidcap
    ```

Install required dependencies:

    ```shell-session
    $ urpmi gcc automake libgtk+2-devel ffmpeg-devel liblame0-devel
    ```

Dirty compile:

    ```shell-session
    $ make distclean [optional]
    $ CPPFLAGS=-I/usr/include/ffmpeg LDFLAGS=-L/usr/bin/ffmpeg
    $ ./configure --with-gtk2 --with-forced-embedded-ffmpeg && make gvidcap
    $ make gvidcap
    $ make install [optional]
    ```

Quick test:

    ```shell-session
    $ ./src/gvidcap &
    ```

## Use gvidcap!

Raw capture:

    ```shell-session
    $ gvidcap --gui no -v --file ~/img_%04d.xwd --frames 0 --fps 10 --cap_geometry 1024x768+0+0
    ```

The following can be used but it slow down the machine (png compression require too cpu):

    ```shell-session
    $ gvidcap --gui no -v --compress 9 --file ~/img_%04d.png --frames 0 --fps 10 --cap_geometry 1024x728+0+0
    ```

Convert .xwd images to .png images because mplayer only support .png, .jpg, .tga and .sgi image file format:

    ```shell-session
    $ convert img_*.xwd img_%04d.png && rm -rf ./*.xwd
    ```

Preview the video:

    ```shell-session
    $ mplayer "mf://*.png" -mf fps=10
    ```

Make a video from successive screenshots:

    ```shell-session
    $ mencoder "mf://*.png" -mf fps=10 -ovc lavc -o ./video.avi
    ```

Documentation:

  * [https://www.linux-magazine.com/issue/45/DeskTOPia_xvidcap.pdf](https://www.linux-magazine.com/issue/45/DeskTOPia_xvidcap.pdf)
  * [https://www.jarre-de-the.net/faq/pdf/faq.pdf](https://www.jarre-de-the.net/faq/pdf/faq.pdf)
  * [https://www.tuxbihan.org/IMG/pdf/gvidcap.pdf](https://www.tuxbihan.org/IMG/pdf/gvidcap.pdf)
  * [https://www.csit.fsu.edu/~beason/recordMovie](https://www.csit.fsu.edu/~beason/recordMovie)
