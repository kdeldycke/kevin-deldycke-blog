---
date: '2013-03-04'
title: Goodnight video
category: English
tags: Music, Video, Kdenlive, slowmoVideo, Omashay, AWS, cloud computing, EC2, ImageMagick, Twixtor, Ubuntu, Kubuntu
---

![]({attach}goodnight-preview.jpg)

A new video has been released by [Omashay](https://omashay.com). Here is Goodnight, on which I did the slow-motion:

https://www.youtube.com/watch?v=bAKmRTV7Lek

The video is [based on a series of 70 sketches](https://omashay.com/2013/02/22/goodnight-the-video/) Tomasito's made for a college project:

![]({attach}goodnight-drawings-keyframes.jpg)

He wanted to explore the possibilities of reusing them for a music video. I had the perfect secret weapon for this kind of job: [slowmoVideo](https://slowmovideo.granjow.net/), an open-source clone of [Twixtor](https://www.revisionfx.com/products/twixtor/).

In fact I tried to use that software 14 months ago, but never went as far as producing something. First I realized I had no nVidia GPU at hand. So I rented a *GPU Quadruple Extra Large* EC2 instance (`cg1.4xlarge`) from Amazon's cloud. It cost me \$4.70 (without VAT) for 3 hours. But I failed to compiles slowmoVideo.

I forgot about it until recently, when I learned it no longer required a GPU to compute the optical flow. And last month I found a way to [compile slowmoVideo on Ubuntu 12.10]({filename}/2013/slowmo-video-ubuntu-12-10.md).

Now it's time to prepare my keyframes. I batch-resized all original drawings to 1080p with a white background. This was done in one command line thanks to ImageMagick:

```shell-session
$ convert -resize 1920x1080 -background white -gravity center -extent 1920x1080 ./keyframes/* pict%04d.png
```

Then I applied a paper texture to add some grain:

```shell-session
$ find ./ -iname "pict*.png" -exec composite -gravity center -compose Multiply ./paper-texture.png "{}" "{}"-texturized.png \;
```

The series of images were imported in slowmoVideo, and I created a 4 minutes linear ultra-slowmotion with the default parameters.

Finally, the raw rendering was assembled in Kdenlive with [Goodnight's audio track](https://omashay.bandcamp.com/track/goodnight) and title cards to produce the result that is now [available on YouTube](https://www.youtube.com/watch?v=bAKmRTV7Lek).
