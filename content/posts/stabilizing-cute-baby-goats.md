date: 2012-02-28 12:18:53
title: Stabilizing Cute Baby Goats
category: English
tags: Canon EOS 7D, Linux, stabilization, transcode, Video

![](/static/uploads/2012/02/newborn-kids-baby-goats-preview.jpg)

## Stabilizing WHAT ?!?

Baby goats. Cute baby goats. Yes, you're reading it right. Look:

http://www.youtube.com/watch?v=el6VMY8KZHo

Yeah, I know, this is a naive video that belongs to [/r/aww](http://www.reddit.com/r/aww/). But any excuse is good to me when its all about playing with video.

These kids (as baby goats are called) decided to come to this world the night I was around. In a hurry I grabbed my [Canon 7D](http://www.amazon.com/gp/product/B002NEGTTW/ref=as_li_tf_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399381&creativeASIN=B002NEGTTW) and filmed these newborns with a [Sigma 30mm f/1.4 EX DC HSM](http://www.amazon.com/gp/product/B0007U0GZM/ref=as_li_tf_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399381&creativeASIN=B0007U0GZM) to leverage its large aperture. And as expected, in the night, with no artificial light and no extra stabilization device, the resulting footage are extremely shaky.

![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B002NEGTTW&camp=217145&creative=399381)

![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B0007U0GZM&camp=217145&creative=399381)

I tried to stabilize the shots but was really disappointed by the results. The final version of the video you watched above only feature the original footage, without any stabilization. But for posterity, here are some notes about the tools I played with.

## vid.stab

![](/static/uploads/2012/01/transcode-stabilizer-log.jpg)

The first tool I tried was [vid.stab](http://public.hronopik.de/vid.stab/), a Transcode plugin that is now part of Transcode itself. But the 1.1.5 version that is bundled with the current Ubuntu 11.10 is quite old.

I wanted to compile it from its [sources](http://github.com/georgmartius/vid.stab). But the [binary distribution](http://public.hronopik.de/vid.stab/download.php) available on the project website works out of the box. To save some effort, let's install the latter:

    :::bash
    $ wget http://public.hronopik.de/vid.stab/files/vid.stab-0.93-transcode-1.1-binary-x86_64.tgz
    $ tar xvzf ./vid.stab-0.93-transcode-1.1-binary-x86_64.tgz
    $ sudo mv ./vid.stab-0.93-transcode-1.1-binary-x84_64/filter_*.so /usr/lib/transcode/
    $ rm -rf ./vid.stab-0.93-transcode-1.1-binary-x8*

Now, as explained in the [documentation](http://public.hronopik.de/vid.stab/features.php), you have to let transcode analyze the video:

    :::bash
    $ transcode -J stabilize -i ./MVI_1714.MOV -y null,null -o dummy

Only after this first pass you can apply the stabilizing transformations:

    :::bash
    $ transcode -J transform -i ./MVI_1714.MOV -y ffmpeg -F huffyuv -o ./MVI_1714-stabilized.MOV

If your not satisfied with the result, you can increase the area of tracking points with the `shakiness` parameter:

    :::bash
    $ transcode -J stabilize=shakiness=8:show=1,preview -i ./MVI_1714.MOV -y null,null -o dummy

In the command line above we added the `show=1,preview` parameters, which have the nice effect of displaying a preview of the work done behind the scene:

![](/static/uploads/2012/02/goat-tracking.jpg)

And if you want to see the transformations applied in the final video, just deactivate the cropping and zooming mechanism:

    :::bash
    $ transcode -J transform=crop=1:optzoom=0 -i ./MVI_1714.MOV -y ffmpeg -F huffyuv -o ./MVI_1714-stabilized.MOV

Finally, here are some command helpers to automate the stabilization process for a massive amount of video:

    :::bash
    $ find ./ -name "*.MOV" -exec transcode -J stabilize -i "{}" -y null,null -o dummy \;
    $ find ./ -name "*.MOV" -exec transcode -J transform -i "{}" -y ffmpeg -F huffyuv -o "{}.stabilized.avi" \;

## Alternative tools

I told you I was disappointed by the results. For example, in the first shot of the video above, `vid.stab` will stabilize based on the movements of the head of the goat, not based on the background. All of this because tracking points are generated on hight-contrast area. Unfortunately in this first scene, the only high contrast area is the kid's head.

Even in shots where the contrast is in our favor, software stabilization don't always produce nice output. If by chance the tracking points are set on the right objects (those that should be considered motionless), the results may not be pleasing, as it may expose inappropriate skewed perspective, shifting motion-blur and spacial deformation.

While a little bit smarter, [YouTube's embedded stabilization effect](http://youtube-global.blogspot.com/2011/03/lights-camera-edit-new-features-for.html) still suffer from these same short-comings. If it  tries to smooth out consecutive transformations better than `vid.stab`, it still fails to produce nice output devoid of unattractive artifacts.

Another tool worth trying is [VirtualDub](http://www.virtualdub.org), which you can run under [Wine](http://www.winehq.org) and leverage its [deshaker plugin](http://www.guthspot.se/video/deshaker.htm). But I didn't tested it.

Last but not least, [Blender can be used to stabilize videos](http://www.youtube.com/watch?v=OJujeSQctEk). Again I haven't tried this yet, but I think it's the best investment of you time, since the new tracking features make Blender a powerful tool for 3D integration.

## Conclusion (tl;dr)

There is no silver bullet: don't expect software stabilizer to save your shaky shots in post-production. If you want steady shots, plan them beforehand and use proper gear on site, be it a monopod, a tripod, a slider, a dolly, a crane or a steadicam. That's the only way to eliminate the pain and deception when you hit the editing room.
