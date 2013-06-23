date: 2013-03-26 12:32:37
title: Tale of Two: production notes
category: English
tags: Kdenlive, linux, omashay, timelapse, slow-motion, slowmoVideo, imagemagick, transcode, vid.stab, Blender

This is the fourth video I've work on for [Omashay](http://omashay.com):

http://www.youtube.com/watch?v=4HtfugU_mGg

This video is a timelapse of a painting Tomasito made in 2007. It's based on a series of photos he took every 10 minutes:

![](/static/uploads/2012/tale-of-two-timelapse.png)


## slowmoVideo

I tried to produce a timelapse out of these images a year ago. In fact, that was the original project I was referring to in my [previous article](http://kevin.deldycke.com/2013/03/goodnight-video/), the project which triggered my initial interest into [slowmoVideo](http://slowmovideo.granjow.net/).

But the experiment failed and I abandoned this endeavor. Instead of slow-motion, and because of the low timing resolution of the photos, I assumed a simple slideshow would do it.


## Blender

The original photos were not consistent. To make them work as a slideshow, they required some stabilization. I tried the new [tracking features of Blender](http://wiki.blender.org/index.php/Doc:2.6/Manual/Motion_Tracking):

![](/static/uploads/2013/blender-timlapse-stabilization.jpg)

While I could feel the power of the tracking tools, my limited knowledge of Blender stopped me. I abandoned this approach. But one day for sure, I'll give Blender the time it deserves.


## vid.stab & Kdenlive

My plan B for stabilization was [Transcode's vid.stab plugin](http://kevin.deldycke.com/2012/02/stabilizing-cute-baby-goats/).

But it can't read images: it only takes videos for input. So we'll produce a video file of a simple slideshow in Kdenlive, then feed the result to vid.stab.

First, in a separate project, I created a stupid slideshow of 1 photo per frame, without any transition:

![](/static/uploads/2012/redux-generation.png)

To keep details, I exported the project to a high-quality h264 stream composed of I-frames only:

![](/static/uploads/2012/export.png)

I wanted to use a true lossless codec here, but after several trials and errors, this profile was the only one <code>vid.stab</code> was able to digest.

I can now apply the stabilization, with a high shakiness parameter to make the algorithm ignore the lack of fluidity:

    :::bash
    $ transcode -J stabilize -i ./slideshow-redux.mp4 -y null,null -o dummy
    $ transcode -J stabilize=shakiness=8 -i ./slideshow-redux.mp4 -y ffmpeg -F huffyuv -o ./slideshow-redux-stabilized.avi

Then we extract all frames of the stabilized video to get a new set of photos:

    :::bash
    $ mkdir ./timelapse-stabilized
    $ cd ./timelapse-stabilized
    $ cp ../slideshow-redux-stabilized.avi
    $ ffmpeg -i ./slideshow-redux-stabilized.avi -f image2 stab%05d.png

From the produced images, I created a new slideshow with proper transitions.

I presented the final rendering to Tomasito, and we agreed that the result, while not incredible, was a good excuse to distribute one of his song on YouTube.

He planned to published the video, but the final editing step was postponed by several months. And then we both forgot the project.


## slowmoVideo, again

Until last January when, after [some efforts](http://kevin.deldycke.com/2013/02/slowmo-video-ubuntu-12-10/), I managed to [produce something with slowmoVideo](http://kevin.deldycke.com/2013/03/goodnight-video/). We resurected the project.

I applied the raw slowmoVideo transformation on the initial set of photos. And the result was good enough. But Tomasito wanted more, and stabilized all the 70 images of the original set by hand !

After this herculean task, I cropped & resized the images to fit the 1080p resolution:

    :::bash
    $ convert -resize 1920x1080 -background black -gravity center -extent 1920x1080 ./manually-stab-keyframes/* pict%04d.png

[As for Goodnight](http://kevin.deldycke.com/2013/03/goodnight-video/), we tried to get rid of the wide black bars on the sides. [QPX](http://wqpx.wordpress.com) created for us a mask made of paint strokes:

![](/static/uploads/2013/video-mask.png)

Then I used that mask to blend the photos with a background fiber texture from [Subtle Patterns](http://subtlepatterns.com):

    :::bash
    $ find ./ -iname "pict*.png" -exec composite "{}" ./stressed_linen-1080p.png ./Masque-02.png "{}"-composed.png \;

Finally I send these pre-rendered keyframes to slowmoVideo to produce a 4 minutes ultra-slow-motion. Then Tomasito added a title and credits.

There is no magic and the final result could have been better if properly shot. What's missing was a steady canvas and good camera positioning, and of course a lower delay between photos. These are the perfect conditions to produce a proper timelapse, and I'm sure we'll demonstrate that in a future project.
