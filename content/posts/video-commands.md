comments: true
date: 2006-11-08 00:31:27
layout: post
slug: video-commands
title: Video commands
wordpress_id: 71
category: English
tags: Audio, CLI, divx, dvd, ffmpeg, kdenlive, Linux, melt, mencoder, mlt, MP4, mplayer, subtitle, svcd, transcode, Video, xvid

  * Here are some commands to get informations about the nature of a video:

        :::bash
        $ mplayer -frames 0 -identify ./video.avi
        $ tcprobe -i ./video.avi
        $ ffmpeg -i ./video.avi
        $ file ./video.avi

## FFmpeg

  * Remux a flash video to an mp4 container without transcoding:

        :::bash
        $ ffmpeg -vcodec copy -acodec copy -i inpout.flv output.mp4

  * Concatenate a series of videos and transcode the audio output to a `flac` file. This [only works with certain multimedia container](http://ffmpeg.org/faq.html#SEC29) (MPEG-1, MPEG-2 PS, DV):

        :::bash
        $ cat M2U01802.MPG M2U01803.MPG M2U01804.MPG | ffmpeg -i - -acodec flac output.flac

  * Remove the first 16 seconds of video and change container to Matroska:

        :::bash
        $ ffmpeg -ss 16 -i ./MVI_8763.MOV -vcodec copy -acodec copy ./MVI_8763.mkv

  * Extract the first frame of a video (great to generate image preview):

        :::bash
        $ ffmpeg -i video.mov -r 1  -t 00:00:01 -f image2 images%05d.png

  * Extract a frame every 10 seconds:

        :::bash
        $ ffmpeg -i video.mov -f image2 -r 1/10 preview-%04d.png

  * Transcode the video stream to the [lossless HuffYUV codec](http://en.wikipedia.org/wiki/Huffyuv):

        :::bash
        $ ffmpeg -i ./MVI_1714.MOV -vcodec huffyuv -sameq ./MVI_1714-lossless.avi

## VLC

  * Transcode the first video stream found in a `m3u` playlist to a 384 kbps MPEG-2 video and 48 kHz Vorbis audio, and serve the resulting stream ina Ogg container to `http://localhost:8888`. To save bandwisth we reduce by two the size of the video:

        :::bash
        $ vlc -vvv http://mafreebox.freebox.fr/freeboxtv/playlist.m3u --sout '#transcode{vcodec=mp2v,vb=384,scale=0.5,acodec=vorbis,ab=48,channels=1}:standard{access=http,mux=ogg,url=:8888}' -I ncurses 2> /dev/null

## Transcode

  * Merge multiple video into one:

        :::bash
        $ avimerge -i part1.avi part2.avi -o big-file.avi

  * Extract the raw subtitle stream. The `-a 0x21` option correspond to the subtitle stream's hexadecimal number (= 0x20 + id of the stream):

        :::bash
        $ tccat -i /space/st-tng/dic1/ -T 1 -L | tcextract -x ps1 -t vob -a 0x22 > subs-en

  * List export video codecs:

        :::bash
        $ transcode -i . -y ffmpeg -F list

## Mplayer / Mencoder

  * Change the aspect ratio of a film for the playback. Standard aspect ratio are : 1.33 (4:3), 1.66 (1.66:1), 1.77 (16:9) and 2.35 (2.35:1):

        :::bash
        $ mplayer -aspect 2:1 ./video.avi

  * Play the video with subtitles:

        :::bash
        $ mplayer -sub ./subtitle_file.txt ./video.avi

  * This will extract audio track no. 128, downmix the AC3 sound to PCM and write the results to `file.wav`:

        :::bash
        $ mplayer -vo null -hardframedrop -aid 128 -ao pcm -aofile file.wav dvd://1

  * This will extract the audio, convert it to PCM and write the resulting wave file to `audio.wav`:

        :::bash
        $ mplayer -vo null -hardframedrop -ao pcm:file=audio.wav myvideo.avi

  * Show all subtitles streams:

        :::bash
        $ mplayer -vo null -ao null -frames 0 -v 2 dvd://1 >&1 | grep sid

  * Create a rotated copy of the `file.avi` video (`rotate=1` : clockwise ; `rotate=2` : anti-clockwise):

        :::bash
        $ mencoder -vop rotate=2 -oac pcm -ovc lavc ./source.avi -o ./dest.avi

  * Preview a video composed of all jpeg files from the current folder at 15fps (mplayer only support jpeg, png, tga and sgi formats):

        :::bash
        $ mplayer "mf://*.jpg" -mf fps=15

  * Create a 15fps video from all jpeg files of the current folder:

        :::bash
        $ mencoder "mf://*.jpg" -mf fps=15 -ovc lavc -o ./dest.avi

  * Encode a SVCD to AVI file:

        :::bash
        $ mencoder -oac lavc -ovc lavc vcd://1 -o ./svcd.avi

  * Transcode video to raw format (be carefull: usually the output video got annoying audio delay):

        :::bash
        $ mencoder -oac pcm -ovc raw -ofps 25 -noskip ./video.wmv -o ./video.avi

  * Encode a video using the default mpeg4 codec at 400 kbps for video and mp3 codec at constant 32 kbps bitrate for audio:

        :::bash
        $ mencoder -oac mp3lame -lameopts cbr:preset=32 -ovc lavc -lavcopts vbitrate=400 in.avi -o out.avi

  * Enhance the sharpness of the video:

        :::bash
        $ mplayer video.avi -vf smartblur=.6:-.5:0,unsharp=l5x5:.8:c5x5:.4

  * Cut a video to keep the first 5.4 seconds:

        :::bash
        $ mencoder big-file.avi -ss 0 -endpos 5.4 -ovc copy -oac copy -o cutted.avi

  * Cut a video to keep everything exept the first 5.4 seconds:

        :::bash
        $ mencoder big-file.avi -ss 5.4 -ovc copy -oac copy -o cutted.avi

  * Show all `mplayer` filter list:

        :::bash
        $ mplayer -vf help

  * Get help of a particular filter (`eq2` in this example):

        :::bash
        $ mplayer -vf eq2=help

  * Here is the filter I use to light up a video taken in the dark with my cheap camera. Of course it add noise but thanks to this we can distinguish shapes in the dark.

        :::bash
        $ mencoder -vf eq2=1.61:1.95:0.54:2.43 -oac pcm -ovc lavc video.avi -o bright-vid.avi

  * And this is the command to preview the result of the filter used above:

        :::bash
        $ mplayer video.avi -vf eq2=1.61:1.95:0.54:2.43

  * This is how I convert raw videos taken with my digital camera into ISO standard MPEG-4 (DivX 5, XVID compatible) videos [to encode in grayscale, add `:gray` option to `-lavcopts`]:

        :::bash
        $ mencoder source.avi -ovc lavc -oac lavc -ffourcc DX50 -lavcopts vcodec=mpeg4:vbitrate=400:v4mv:mbd=2:trell:autoaspect:dia=2:acodec=mp3:abitrate=32:vpass=1 -vf hqdn3d -o output.avi
        $ mencoder source.avi -ovc lavc -oac lavc -ffourcc DX50 -lavcopts vcodec=mpeg4:vbitrate=400:v4mv:mbd=2:trell:autoaspect:dia=2:acodec=mp3:abitrate=32:vpass=2 -vf hqdn3d -o output.avi

  * Play all videos of the current folder fullscreen at 4x speed with 50% more brightness:

        :::bash
        $ mplayer -speed 4 -brightness 50 -fs ./*.avi

  * Extract audio stream from a video:

        :::bash
        $ mplayer -dumpaudio -dumpfile audio.ac3 video_source.mpg

## Others

  * List MLT audio codecs:

        :::bash
        $ melt -query "audio_codecs"

  * Extract to `chapter.txt` the chapter file of the track n°1 of the DVD:

        :::bash
        $ dvdxchap -t 1 /mnt/cdrom > chapter.txt

  * Test XV video driver output via gstreamer v0.10:

        :::bash
        $ gst-launch-0.10 videotestsrc ! xvimagesink

