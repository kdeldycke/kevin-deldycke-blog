---
date: 2006-11-08 00:31:27
title: Video commands
category: English
tags: Audio, CLI, divx, dvd, ffmpeg, Kdenlive, Linux, melt, mencoder, mlt, MP4, mplayer, subtitle, svcd, transcode, Video, xvid, TV, VLC
---

  * Here are some commands to get informations about the nature of a video:

        :::bash
        $ ffmpeg -i ./video.avi
        $ file ./video.avi
        $ avprobe ./video.avi
        $ mplayer -frames 0 -identify ./video.avi
        $ tcprobe -i ./video.avi


## FFmpeg

  * Remux a flash video to an mp4 container without transcoding:

        :::bash
        $ ffmpeg -vcodec copy -acodec copy -i inpout.flv output.mp4
 
  * Remove audio:

        :::bash
        $ ffmpeg -i ./input.mp4 -an -vcodec copy ./input-no-audio.mp4

  * Concatenate a series of videos and transcode the audio output to a `flac`
  file. This [only works with certain multimedia
  container](https://ffmpeg.org/faq.html#SEC29) (MPEG-1, MPEG-2 PS, DV):

        :::bash
        $ cat M2U01802.MPG M2U01803.MPG M2U01804.MPG | ffmpeg -i - -acodec flac output.flac

  * Remove the first 16 seconds of video and change container to Matroska:

        :::bash
        $ ffmpeg -ss 16 -i ./MVI_8763.MOV -vcodec copy -acodec copy ./MVI_8763.mkv

  * Extract the first frame of a video (great to generate image preview):

        :::bash
        $ ffmpeg -i video.mov -r 1 -t 00:00:01 -f image2 images%05d.png

  * Extract a frame every 10 seconds:

        :::bash
        $ ffmpeg -i video.mov -f image2 -r 1/10 preview-%04d.png

  * Transcode the video stream to the [lossless HuffYUV codec](https://en.wikipedia.org/wiki/Huffyuv):

        :::bash
        $ ffmpeg -i ./MVI_1714.MOV -vcodec huffyuv -sameq ./MVI_1714-lossless.avi

  * Produce a dummy 10 seconds video of a solid pink background at 1080p/60fps:

        :::bash
        $ ffmpeg -f lavfi -i "color=color=pink:size=1920x1080" -r 60 -t 10 -c:v libx264 dummy.mp4

  * Produce a video from a static image and an audio file. That's the way I produced [Cool Cavemen's video tracks](https://www.youtube.com/channel/UCklBE-RIZESco4bp5kg80eA) for YouTube. Hence the special video filter option which [crop the image](http://ffmpeg.org/ffmpeg-filters.html#crop) to a square (thanks to [arithmetic operators](http://ffmpeg.org/ffmpeg-utils.html#Expression-Evaluation)) and [scale it](http://ffmpeg.org/ffmpeg-filters.html#scale-1) to a 1080x1080 pixels video:

        :::bash
        $ ffmpeg -loop 1 -y -i ./album-front-cover.jpg -i ./track-01.flac -c:v libx264 -tune stillimage -vf "crop='min(in_h,in_w)':'min(in_h,in_w)',scale=-2:1080" -c:a copy -shortest ./track-01-video.mkv

  * Same as above but instead of cropping, [pad](http://ffmpeg.org/ffmpeg-filters.html#toc-pad-1) with either vertical or horizontal [black](http://ffmpeg.org/ffmpeg-utils.html#Color) bars to fit a typical Full HD 1080p steam of 1920x1080 pixels:

        :::bash
        $ ffmpeg -loop 1 -y -i ./album-front-cover.jpg -i ./track-01.flac -c:v libx264 -tune stillimage -vf "scale=-2:1080:force_original_aspect_ratio=1,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black" -c:a copy -shortest ./track-01-video.mkv

  * Extract a segment of a video and produce a gif animation out of it. The extracted fragment is from the absolute time reference of `00:24:52.4` to `00:24:57.0`. The first video stream is selected (`[0:v]`), and the audio naturraly discarded. Framerate is reduced to 12 fps, and horizontal size to 480 pixels while keeping the aspect ratio. It use special filters to [generate a global optimized color palette](http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html) limited to 64 colors. The first subtitle track (`si=0`) embedded in the original `source.mp4` file is burned down, in a bold Arial Black font at 26pt (as per [ASS specs](http://moodub.free.fr/video/ass-specs.doc)).

        :::bash
        $ ffmpeg -i ./source.mp4 -ss 00:24:52.4 -to 00:24:57.0 -filter_complex "[0:v] fps=12,scale=width=480:height=-1:flags=lanczos,subtitles=source.mp4:si=0:force_style='FontName=Arial Black,Bold=-1,FontSize=26',split [a][b];[a] palettegen=64 [p];[b][p] paletteuse" ./meme.gif

      To pinpoint the right moment to cut your segment, here is a variation of the above to produce a set of timecoded frames with embeded subtitles for preview:
  
        :::bash
        $ ffmpeg -i ./source.mp4 -ss 00:24:52.700 -to 00:24:57.371 -filter_complex "drawtext=text='%{pts\:hms}': fontcolor=black: fontsize=32: box=1: boxcolor=white,subtitles=source.mp4:si=0" -f image2 "%04d.jpg"


## VLC

  * Transcode the first video stream found in a `m3u` playlist to a 384 kbps
  MPEG-2 video and 48 kHz Vorbis audio, and serve the resulting stream ina Ogg
  container to `http://localhost:8888`. To save bandwidth we reduce by two the
  size of the video:

        :::bash
        $ vlc -vvv https://mafreebox.freebox.fr/freeboxtv/playlist.m3u --sout '#transcode{vcodec=mp2v,vb=384,scale=0.5,acodec=vorbis,ab=48,channels=1}:standard{access=http,mux=ogg,url=:8888}' -I ncurses 2> /dev/null


## libAV

  * Re-encode a yuv422p video into a lossless h264, but this time in yuv420p:

        :::bash
        $ avconv -i yuv422p.mkv -c:v libx264 -pix_fmt yuv420p -preset veryslow -qp 0 yuv420p.mkv

  * Re-encode a lossless h264 video with a lower bitrate:

        :::bash
        $ avconv -i lossless.mkv -b:v 45M -preset veryfast lower-bitrate.mkv


## Mplayer / Mencoder

  * Change the aspect ratio of a film for the playback. Standard aspect ratio
  are : 1.33 (4:3), 1.66 (1.66:1), 1.77 (16:9) and 2.35 (2.35:1):

        :::bash
        $ mplayer -aspect 2:1 ./video.avi

  * Play the video with subtitles:

        :::bash
        $ mplayer -sub ./subtitle_file.txt ./video.avi

  * This will extract audio track no. 128, downmix the AC3 sound to PCM and
  write the results to `file.wav`:

        :::bash
        $ mplayer -vo null -hardframedrop -aid 128 -ao pcm -aofile file.wav dvd://1

  * This will extract the audio, convert it to PCM and write the resulting wave
  file to `audio.wav`:

        :::bash
        $ mplayer -vo null -hardframedrop -ao pcm:file=audio.wav myvideo.avi

  * Show all subtitles streams:

        :::bash
        $ mplayer -vo null -ao null -frames 0 -v 2 dvd://1 >&1 | grep sid

  * Create a rotated copy of the `file.avi` video (`rotate=1`: clockwise;
  `rotate=2`: anti-clockwise):

        :::bash
        $ mencoder -vop rotate=2 -oac pcm -ovc lavc ./source.avi -o ./dest.avi

  * Preview a video composed of all jpeg files from the current folder at 15fps
  (mplayer only support jpeg, png, tga and sgi formats):

        :::bash
        $ mplayer "mf://*.jpg" -mf fps=15

  * Create a 15fps video from all jpeg files of the current folder:

        :::bash
        $ mencoder "mf://*.jpg" -mf fps=15 -ovc lavc -o ./dest.avi

  * Encode a SVCD to AVI file:

        :::bash
        $ mencoder -oac lavc -ovc lavc vcd://1 -o ./svcd.avi

  * Transcode video to raw format (be carefull: usually the output video got
  annoying audio delay):

        :::bash
        $ mencoder -oac pcm -ovc raw -ofps 25 -noskip ./video.wmv -o ./video.avi

  * Encode a video using the default mpeg4 codec at 400 kbps for video and mp3
  codec at constant 32 kbps bitrate for audio:

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

  * Here is the filter I use to light up a video taken in the dark with my
  cheap camera. Of course it add noise but thanks to this we can distinguish
  shapes in the dark.

        :::bash
        $ mencoder -vf eq2=1.61:1.95:0.54:2.43 -oac pcm -ovc lavc video.avi -o bright-vid.avi

  * And this is the command to preview the result of the filter used above:

        :::bash
        $ mplayer video.avi -vf eq2=1.61:1.95:0.54:2.43

  * This is how I convert raw videos taken with my digital camera into ISO
  standard MPEG-4 (DivX 5, XVID compatible) videos (to encode in grayscale, add
  `:gray` option to `-lavcopts`):

        :::bash
        $ mencoder source.avi -ovc lavc -oac lavc -ffourcc DX50 -lavcopts vcodec=mpeg4:vbitrate=400:v4mv:mbd=2:trell:autoaspect:dia=2:acodec=mp3:abitrate=32:vpass=1 -vf hqdn3d -o output.avi
        $ mencoder source.avi -ovc lavc -oac lavc -ffourcc DX50 -lavcopts vcodec=mpeg4:vbitrate=400:v4mv:mbd=2:trell:autoaspect:dia=2:acodec=mp3:abitrate=32:vpass=2 -vf hqdn3d -o output.avi

  * Play all videos of the current folder fullscreen at 4x speed with 50% more
  brightness:

        :::bash
        $ mplayer -speed 4 -brightness 50 -fs ./*.avi

  * Extract audio stream from a video:

        :::bash
        $ mplayer -dumpaudio -dumpfile audio.ac3 video_source.mpg


## Transcode

  * Merge multiple video into one:

        :::bash
        $ avimerge -i part1.avi part2.avi -o big-file.avi

  * Extract the raw subtitle stream. The `-a 0x21` option correspond to the
  subtitle stream's hexadecimal number (= 0x20 + id of the stream):

        :::bash
        $ tccat -i /space/st-tng/dic1/ -T 1 -L | tcextract -x ps1 -t vob -a 0x22 > subs-en

  * List export video codecs:

        :::bash
        $ transcode -i . -y ffmpeg -F list

  * Batch stabilization script:

        :::bash
        SEARCH_FOLDER="/home/kevin/project/raw_sources"
        DEST_FOLDER="/home/kevin/project/stabilized"

        for FILE_PATH in $(find "$SEARCH_FOLDER" -name "*.mp4")
        do
            FILE_NAME=$(basename "$FILE_PATH")

            STAB_FILE="$DEST_FOLDER/$FILE_NAME.trf"
            if [ ! -e "$STAB_FILE" ]; then
                # vis.stab's deshake/stabilize documentation:
                # https://github.com/georgmartius/vid.stab/blob/36173857bfc0fa111983a5934f2cc6322969e928/transcode/filter_deshake.c#L75-L106
                transcode -J stabilize=result="$STAB_FILE" -i "$FILE_PATH" -y null,null -o dummy
            fi

            FINAL_FILE="$DEST_FOLDER/$FILE_NAME-stabilized.mkv"

            if [ ! -e "$FINAL_FILE" ]; then

                # Create a stabilized stream of JPG files at 100% quality.
                FRAME_BASEPATH="$DEST_FOLDER/$FILE_NAME.stabilized_"
                # vid.stab's transform documentation:
                # https://github.com/georgmartius/vid.stab/blob/36173857bfc0fa111983a5934f2cc6322969e928/src/transform.h#L122-L149
                transcode -J transform=input="$STAB_FILE" -i "$FILE_PATH" -y jpg,null -F 100 -o "$FRAME_BASEPATH"

                # Convert to a lossless h264 video in 4:2:0 color space.
                FRAME_RATE=$(tcprobe -i "$FILE_PATH" | grep "frame rate:" | cut -d ':' -f 2 | cut -d ' ' -f 3)
                avconv -r $FRAME_RATE -i "$FRAME_BASEPATH%06d.jpg" -c:v libx264 -pix_fmt yuv420p -preset veryfast -qp 0 "$FINAL_FILE"

                find "$DEST_FOLDER" -name "$FRAME_BASENAME*.jpg" -delete

            fi

        done


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
