date: 2013-02-19 12:02:07
title: How-To Compile slowmoVideo on Ubuntu 12.10
category: English
tags: video, Slow Motion, Ubuntu, Ubuntu 12.10, Kubuntu, aptitude, apt-get, shell, Twixtor

[slowmoVideo](http://slowmovideo.granjow.net) is an open-source equivalent of the well-known proprietary [Twixtor plugin](http://www.revisionfx.com/products/twixtor/).

If you try to follow the [procedure from the project documentation](http://slowmovideo.granjow.net/download.php#h2_Compiling) under Kubuntu 12.10, you'll not go very far. Because you'll start by installing the default `-dev` packages of `libavutil`:

    :::bash
    $ sudo aptitude install libavcodec-dev libavdevice-dev libavfilter-dev libavformat-dev libavutil-dev libswscale-dev

Then you'll need the `-extra` packages, which can't be installed with `-dev` packages:

    :::bash
    $ sudo aptitude install libavcodec-extra-53
    The following NEW packages will be installed:
      libavcodec-extra-53{b} libavutil-extra-51{ab} libvo-aacenc0{a} libvo-amrwbenc0{a}
    0 packages upgraded, 4 newly installed, 0 to remove and 0 not upgraded.
    Need to get 3,278 kB of archives. After unpacking 8,006 kB will be used.
    The following packages have unmet dependencies:
    libavutil51 : Conflicts: libavutil-extra-51 but 6:0.8.5ubuntu0.12.10.1 is to be installed.
    libavutil-extra-51 : Conflicts: libavutil51 but 6:0.8.5-0ubuntu0.12.10.1 is installed.
    libavcodec53 : Conflicts: libavcodec-extra-53 but 6:0.8.5ubuntu0.12.10.1 is to be installed.
    libavcodec-extra-53 : Conflicts: libavcodec53 but 6:0.8.5-0ubuntu0.12.10.1 is installed.
    The following actions will resolve these dependencies:

        Keep the following packages at their current version:
    1)     libavcodec-extra-53 [Not Installed]
    2)     libavutil-extra-51 [Not Installed]

    Accept this solution? [Y/n/q/?] q
    Abandoning all efforts to resolve these dependencies.
    Abort.

This [issue was already reported](https://bugs.launchpad.net/ubuntu/+source/libav/+bug/1038781). But we're lucky: someone contributed on that ticket a [nice script](https://launchpadlibrarian.net/126008181/mk_libav-extra-dev.sh) to help you build the missing link.

Let's fetch it and make it produce a collection of new `libav` packages:

    :::bash
    $ mkdir new_libav
    $ cd new_libav
    $ wget https://launchpadlibrarian.net/126008181/mk_libav-extra-dev.sh
    $ chmod 755 ./mk_libav-extra-dev.sh
    $ ./mk_libav-extra-dev.sh

You can then install the working `libav` packages:

    :::bash
    $ sudo dpkg --install ./lib*.deb
    $ cd ..
    $ rm -rf ./new_libav

Now, we can follow the standard slowmoVideo instructions:

    :::bash
    $ sudo aptitude install build-essential cmake git ffmpeg libavformat-dev libavcodec-dev libswscale-dev libqt4-dev freeglut3-dev libglew1.5-dev libsdl1.2-dev libjpeg-dev libopencv-video-dev libopencv-highgui-dev
    $ cd ~
    $ git clone git://github.com/slowmoVideo/slowmoVideo.git
    $ cd slowmoVideo/slowmoVideo
    $ mkdir build
    $ cd build
    $ sudo aptitude install libopencv-dev
    $ cmake ..
    $ make -j3
    $ make install
    $ cd ../../V3D
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make -j3
    $ make install

After that you'll be able to run slowmoVideo itself:

    $ ~/slowmoVideo/install/bin/slowmoUI

![slowmoVideo timeline screenshot](/static/uploads/2013/slowmo-video-timeline.png)
