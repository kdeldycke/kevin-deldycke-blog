---
date: 2013-07-01 12:48
title: How-to keep natural glitches from videos
category: English
tags: Kdenlive, mplayer, avconv, libav, ffmpeg, video, YouTube, audio

In my ultimate attempt to recover the archives I lost some years ago in a RAID-5 crash, I managed to save some images and videos. But most files, if not all, were heavily corrupted.

Some of the natural glitches introduced were interesting. I decided to test some approach to save these natural glitches.

Here is one video resulting of these experimentations:

http://www.youtube.com/watch?v=zVaXnD7PxHI

To generate this video, I first extracted all frames to PNG and moved them to a dedicated folder:

    :::bash
    $ mplayer -vo png ./corrupted_video.mpg
    $ mkdir frames
    $ mv ./*.png ./frames/

Then I simply recombined the individual frames to a video:

    :::bash
    $ avconv -f image2 -framerate 25 -i ./frames/%08d.png -s 720x576 -vcodec huffyuv -same_quant export_lossless.avi

I extracted the audio too:

    :::bash
    $ mplayer -vo null -hardframedrop -ao pcm:file=audio.wav ./corrupted_video.mpg

Finally I edited and recombined the video and audio in Kdenlive, to cut out long and uninteresting parts.
