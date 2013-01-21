comments: true
date: 2006-11-01 00:43:08
layout: post
slug: audio-commands
title: Audio commands
wordpress_id: 72
category: English
tags: alac, asf, Audio, CLI, cue-list, flac, Linux, lossless, midi, Ogg, shntool, sox, wave




  * Convert `.ape` file to `.wav`:

    
    :::console
    ffmpeg -i audio.ape audio.wav
    






  * Split a one-file album flac file into tracks according its cue list:

    
    :::console
    shntool split -f album.cue -o flac album.flac
    






  * Merge several .wav file to one file named `merged.wav`:

    
    :::console
    sox part1.wav part2.wav part3.wav merged.wav
    






  * Convert `.wav` audio file to ALAC lossless file:

    
    :::console
    ffmpeg -i audio.wav -acodec alac audio.m4a
    






  * Convert `.asf` audio file to PCM wave file:

    
    :::console
    mplayer -vo null -hardframedrop -ao pcm:file=audio.wav audio.asf
    






  * Convert MIDI file to Ogg/Vorbis:

    
    :::console
    timidity -Ov1S *.mid
    






  * Extract the Right then Left channel of a stereo .wav file:

    
    :::console
    sox stereo.wav -c 1 rightchan.wav avg -r
    sox stereo.wav -c 1 leftchan.wav avg -l
    






  * Some sox compressor parameters:

    
    :::console
    play audio.wav compand .1,.1 -60,-10 0 0 .1
    play audio.wav compand .01,.3 -6,-4,-3,-3,0,-3
    play audio.wav compand 0.3,1 -90,-90,-70,-70,-60,-20,0,0 -5 0 0.2
    






  * Test Alsa audio driver output via gstreamer v0.10:

    
    :::console
    gst-launch-0.10 audiotestsrc ! alsasink
    






  * Generate cyclic pink noise ([source](http://news.ycombinator.com/item?id=3547169)):

    
    :::console
    play -t sl -r48000 -c2 - synth -1 pinknoise tremolo .1 40 <  /dev/zero
    






  * Generate background low frequency noise ([source](http://news.ycombinator.com/item?id=3547169)):

    
    :::console
    play -c2 -n synth whitenoise band -n 100 24 band -n 300 100 gain +20
    







Other related ressources:

  
  * [Sox examples](http://linuxcommand.org/man_pages/soxexam1.html)

  
  * [Audio Processing Pipelines](http://linuxgazette.net/issue73/chung.html)


