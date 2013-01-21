comments: true
date: 2006-04-10 00:30:38
layout: post
slug: av-sync-problems-vlc-better-than-mencoder
title: A/V sync problems: VLC better than Mencoder
wordpress_id: 3
category: English
tags: Linux, mencoder, Video, VLC

Today I tried to transcode a bunch of videos using my favorite script. I need to do this because the videos produced with my cheap camera use Mjpeg as video codec and raw-data as audio codec. This result of incredible large files. To share my videos with friends, I transcode them to mpeg4/mp3 files. This is all the dirty work my script is supposed to handle.

Unfortunately I didn't use it since I upgraded Mandriva from 2005 to the 2006 release. As you can guess, it wasn't working: mencoder gave me the following "Audio LAVC, couldn't find encoder for codec mp3" error message. First, I though it was because of a bad version of ffmpeg. Looking at the source RPM from PLF repository gave me the proof that my version was compiled with the right options.

To bypass this problems, I used the -mp3lame as output audio codec. This introduced horrible A/V sync. :( For 3 hours, I tried to play with mencoder options without success. I was completetly desesperated... until I tried VLC. In less than 10 minutes I was able to get the expected result: perfect A/V sync movie file !

Thanks to the [VLC wiki](http://wiki.videolan.org/index.php/Main_Page), I also discovered the h264 video codec, which is a good codec for low bitrates. Even if it produce bigger files compared to my older method (the latter can be found in [the first version of the script](http://kevin.deldycke.com/static/scripts/avi2mp4-2005_10_02.py)), the quality is very awesome and video artefacts (ringings and blockings) are so reduced that it's now very hard to distinguish. So I decided to use h264 in the [new version of my script](http://kevin.deldycke.com/static/scripts/avi2mp4-2006_04_09.py).

There is still an inconvenient of using VLC instead of mencoder: VLC is transcoded at real time ! I tried the "hurry-up" parameters without effects. This is sad but acceptable, since my goal is to archive my tiny videos.

To summarize, here is the command line I use to do transcoding via VLC:

    
    :::console
    vlc --sout-all "input_video.avi" :sout='#transcode{vcodec=h264, acodec=mp3, ab=32,channels=1, audio-sync}:std{access=file, mux=mp4, url="output_video.mp4"}' vlc:quit -I dummy
    



This command is far from perfect and I plan to dig into VLC help to tune h264 codec.

