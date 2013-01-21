comments: true
date: 2005-06-27 13:41:39
layout: post
slug: howto-compile-and-use-xvidcap
title: How-to Compile and Use xvidcap
wordpress_id: 67
category: English
tags: CLI, Linux, Mandriva, mencoder, mplayer, Video, xvidcap

## Compile gvidcap !



Get the last stable source code archive on [xvidcap Sourceforge project page](http://sourceforge.net/projects/xvidcap) or download it from the [CVS](http://cvs.sourceforge.net/viewcvs.py/xvidcap):

    
    :::console
    cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/xvidcap co -P xvidcap
    



Install required dependencies:

    
    :::console
    urpmi gcc automake libgtk+2-devel ffmpeg-devel liblame0-devel
    



Dirty compile:

    
    :::console
    make distclean [optional]
    CPPFLAGS=-I/usr/include/ffmpeg LDFLAGS=-L/usr/bin/ffmpeg
    ./configure --with-gtk2 --with-forced-embedded-ffmpeg && make gvidcap
    make gvidcap
    make install [optional]
    



Quick test:

    
    :::console
    ./src/gvidcap &
    






## Use gvidcap !



Raw capture:

    
    :::console
    gvidcap --gui no -v --file ~/img_%04d.xwd --frames 0 --fps 10 --cap_geometry 1024x768+0+0
    



The following can be used but it slow down the machine (png compression require too cpu):

    
    :::console
    gvidcap --gui no -v --compress 9 --file ~/img_%04d.png --frames 0 --fps 10 --cap_geometry 1024x728+0+0
    



Convert .xwd images to .png images because mplayer only support .png, .jpg, .tga and .sgi image file format:

    
    :::console
    convert img_*.xwd img_%04d.png && rm -rf ./*.xwd
    



Preview the video:

    
    :::console
    mplayer "mf://*.png" -mf fps=10
    



Make a video from successive screenshots:

    
    :::console
    mencoder "mf://*.png" -mf fps=10 -ovc lavc -o ./video.avi
    



Documentation:


  * [http://www.linux-magazine.com/issue/45/DeskTOPia_xvidcap.pdf](http://www.linux-magazine.com/issue/45/DeskTOPia_xvidcap.pdf)


  * [http://www.jarre-de-the.net/faq/pdf/faq.pdf](http://www.jarre-de-the.net/faq/pdf/faq.pdf)


  * [http://www.tuxbihan.org/IMG/pdf/gvidcap.pdf](http://www.tuxbihan.org/IMG/pdf/gvidcap.pdf)


  * [http://www.csit.fsu.edu/~beason/recordMovie](http://www.csit.fsu.edu/~beason/recordMovie)
