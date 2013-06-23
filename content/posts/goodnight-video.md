date: 2013-03-04 12:31:36
title: Goodnight video
category: English
tags: Music, Video, Kdenlive, slowmoVideo, Omashay, AWS, Amazon, cloud computing, EC2, ImageMagick, Twixtor, Ubuntu, Kubuntu

A new video has been released by [Omashay](http://omashay.com). Here is Goodnight, on which I did the slow-motion:

http://www.youtube.com/watch?v=bAKmRTV7Lek

The video is [based on a series of 70 sketches](http://omashay.com/2013/02/22/goodnight-the-video/) Tomasito's made for a college project:

![](/static/uploads/2013/goodnight-drawings-keyframes.jpg)

He wanted to explore the possibilities of reusing them for a music video. I had the perfect secret weapon for this kind of job: [slowmoVideo](http://slowmovideo.granjow.net/), an open-source clone of [Twixtor](http://www.revisionfx.com/products/twixtor/).

In fact I tried to use that software 14 months ago, but never went as far as producing something. First I realized I had no <a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=nVidia%20GPU&linkCode=ur2&tag=kevideld-20&url=search-alias%3Daps">nVidia GPU</a><img src="https://www.assoc-amazon.com/e/ir?t=kevideld-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> at hand. So I rented a *GPU Quadruple Extra Large* EC2 instance (`cg1.4xlarge`) from Amazon's cloud. It cost me $4.70 (without VAT) for 3 hours. But I failed to compiles slowmoVideo.

I forgot about it until recently, when I learned it no longer required a GPU to compute the optical flow. And last month I found a way to [compile slowmoVideo on Ubuntu 12.10](http://kevin.deldycke.com/2013/02/slowmo-video-ubuntu-12-10/).

Now it's time to prepare my keyframes. I batch-resized all original drawings to 1080p with a white background. This was done in one command line thanks to <a target="_blank" href="http://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=ImageMagick&linkCode=ur2&rh=i%3Aaps%2Ck%3AImageMagick&tag=kevideld-20&url=search-alias%3Daps">ImageMagick</a><img src="https://www.assoc-amazon.com/e/ir?t=kevideld-20&l=ur2&o=1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />:

    :::bash
    $ convert -resize 1920x1080 -background white -gravity center -extent 1920x1080 ./keyframes/* pict%04d.png

Then I applied a paper texture to add some grain:

    :::bash
    $ find ./ -iname "pict*.png" -exec composite -gravity center -compose Multiply ./paper-texture.png "{}" "{}"-texturized.png \;

The series of images were imported in slowmoVideo, and I created a 4 minutes linear ultra-slowmotion with the default parameters.

Finally, the raw rendering was assembled in Kdenlive with [Goodnight's audio track](http://omashay.bandcamp.com/track/goodnight) and title cards to produce the result that is now [available on YouTube](http://www.youtube.com/watch?v=bAKmRTV7Lek).