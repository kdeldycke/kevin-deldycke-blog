---
date: 2010-09-29 15:28:15
title: Making of "Info TGV" Android app video
category: English
tags: Android, Canon EOS 7D, ffmpeg, HTC, Kdenlive, Kubuntu, Ubuntu, Linux, Twitter, Uperto, Video, x264, YouTube, SoundUp studio
---

Last week I was called by one of my co-worker from [Uperto](http://www.uperto.com) (the open-source division of [Devoteam](http://devoteam.com)). He knew I worked on some [video projects for my band](http://www.youtube.com/user/coolcavemen), so he asked me if I wanted to help him create one. The video was meant to be released 5 days later, so we clearly were in a hurry. However this was a great oportunity to play with my [Canon EOS 7D](http://amzn.com/B002NEGTTW/?tag=kevideld-20), so I accepted! :)



The goal of the video was to show off an [Android application we made](http://pro.01net.com/editorial/519142/concours-d-application-smartphone-sncf-les-candidats-sur-les-starting-blocks/), for a [contest organized by SNCF](http://www.01net.com/statiquesv6/sncf/pres.html) (the [french national railroad](http://en.wikipedia.org/wiki/Sncf)). The application, that we simply named _Info TGV_, is designed to centralize informations for on-board staff. This application will give train personnel better insights when delays or other kind of traffic perturbations arise.

Here is the final video we managed to create:

http://www.youtube.com/watch?v=puDy-twV-Y4

Now let's talk about what happened behind the scenes! :)

## Shooting

In all of my projects, I want to use free and open-source software, and push their usage for every step of the creation workflow. For video recording, there is no open-source firmware for the 7D. Sadly, the [Magic Lantern](http://magiclantern.wikia.com) community seems to have [reached a dead-end regarding 7D support](http://groups.google.com/group/ml-devel/browse_thread/thread/648f25d8d543e58). I'm quite sad as I choosed the 7D a year ago for 2 things: its video capabilities and the potential hackability of this camera (extrapolating Magic Lantern's success on the [5D Mark II](http://amzn.com/B001G5ZTLS/?tag=kevideld-20)). But this doesn't stop me to get usable footages. Far from it.



For this video, I choose to use my [Sigma 30mm f/1.4 lens](http://amzn.com/B0007U0GZM/?tag=kevideld-20) as it's the fastest lens I have today.

 I wanted to reduce the depth of field as much as I can to emphasize the screen of the [HTC Desire](http://amzn.com/B0038JDF3E/?tag=kevideld-20), as all the important "action" takes place in the plane of the phone's screen.



So I set my 7D to record in 1080p at 25 fps, open the lens at f/1.4 and set the shutter speed to a [traditional 1/50s](http://en.wikipedia.org/wiki/Shutter_angle). I then set the ISO to 160 (which is the lowest [native ISO value available on the 7D](http://brendanhbanks.tumblr.com/post/392272676/the-5d-and-7ds-native-iso-levels-are-160-320)). Still, the final image was over-exposed so I attached a [variable ND-filter](http://amzn.com/B003RDF2MS/?tag=kevideld-20) to the lens and tuned it until I had an acceptable result. I finally customized the white balance to match the ambient light temperature.



Here is a snapshot of this first test on my [Samsung Galaxy S](http://amzn.com/B003SIDVRA/?tag=kevideld-20) (notice the strong [vignetting](http://en.wikipedia.org/wiki/Vignetting) created by the ND-filter):



![](/uploads/2010/original-video-settings.png)

Here is how this first test setup looked like:

![](/uploads/2010/2010-09-20-17.30.40.jpg)

All these parameters were calibrated for an afternoon shooting session, but we really started to record in the evening (look at the phone's clock in the video!). Because of this delay, I lost the white stripe of natural light coming from the top of the background. At the last minute, I started to play with the white balance. Then I changed my mind and removed the ND-filter. And closed the lens to f/3.5 to get a more manageable depth of field. In a word, I messed up all my initial settings resulting in a final video looking worse (in my opinion) compared to my first test. _The better is the enemy of the good_...

But there is something I'm quite happy with from my last minute changes: dimming the phone's screen brightness. Phone screens are so powerful nowadays that they create [clipped highlights](http://en.wikipedia.org/wiki/Clipping_(photography)), thus reducing the readability of black characters on white background.

Here is a photo of the final setup, in which I marked the focus plan with black electric tape:

![](/uploads/2010/2010-09-21-15.25.45.jpg)

As you can see in the final video, I have some aliasing issues due to the [pixelated nature of the phone's screen](http://en.wikipedia.org/wiki/Active-matrix_OLED) and the [line skipping happening on 7D's CMOS sensor](http://vimeo.com/11000025). I tried to reduce the aliasing by moving the phone to a distance were the natural softness of the Sigma lens will occur. I didn't really succeed as it's really hard to maintain a constant distance to the lens while holding the phone by hand.

Yes, I could have tried to put the phone on a stand but I really wanted to show the app on a real phone, into real hands, as to make it clear there was no special effects or compositing in action. The application is real, it's running on bare metal, it's not a mockup, showing that Uperto has tough engineers getting things done! ;)

By the way, about hands: there a trick involved here. The left hand is mine, but the right one is my co-worker's. There was a big advantage using this technic: with an eye on the 7D's rear LCD monitor, I can fully concentrate on the image and micro-adjust the distance of the phone to the lens. In the same time, my co-worker can focus (pardon the pun) on the action and follow the script. The only time when you can see my right hand is when I take the [Acer Liquid E](http://mobile.acer.com/en/phones/liquide/) to demonstrate the propagation of messages via Twitter:

![](/uploads/2010/htc-desire-and-acer-liquid-e.png)

## Video editing

For video editing, I knew I'll not be able to manipulate my 7D's files natively. At least not with the default packages bundled with my [Kubuntu 10.04](http://www.kubuntu.org/news/10.04-lts-release). So monday morning I started to compile the trunk version of [x264](http://www.videolan.org/developers/x264.html), [FFmpeg](http://ffmpeg.org) and [MLT](http://mltframework.org). Then I realized a brand new version of [Kdenlive (v0.7.8) was released](http://www.kdenlive.org/users/j-b-m/kdenlive-078-released). How did I missed such an important news about my favorite [NLE](http://en.wikipedia.org/wiki/Video_editing_software) ? :) Compliments must go to the Kdenlive team for providing up to date packages and all their dependencies!

So I did the entire video editing with Kdenlive. Here is what the final project looks like in the timeline:

![](/uploads/2010/kdenlive-info-tgv-project-timeline.png)

Inter-title cards were created from scratch with [Gimp](http://www.gimp.org):

![](/uploads/2010/gimp-title-card-editing.png)

## Audio

Let's talk audio now. I personally want to thanks [Tomasito, Cool Cavemen's saxophonist](http://coolcavemen.com/biography/tomasito/), who lends me his [Shure Beta57A microphone](http://amzn.com/B0002BACAK/?tag=kevideld-20) and his [Line 6 POD Studio UX1](http://amzn.com/B001EKECAY/?tag=kevideld-20) interface for this project. With [electrical tape](http://en.wikipedia.org/wiki/Electrical_tape), I attached the microphone on my [Gorillapod](http://amzn.com/B002FGTWOC/?tag=kevideld-20), which serves as a mic stand. I used this setup to record Arnaud's voice:







![](/uploads/2010/shure-beta-57a-microphone-on-gorillapod.jpg)

I wanted to record the speach on my linux machine but I didn't managed to compile the [Line 6 open-source drivers](http://line6.com/community/thread/4031). In fact the module compiled but refused to load:

    :::text
    Sep 20 22:02:47 kev-laptop kernel: [  717.905187] line6usb: Unknown symbol snd_rawmidi_receive
    Sep 20 22:02:47 kev-laptop kernel: [  717.905321] line6usb: disagrees about version of symbol snd_ctl_add
    Sep 20 22:02:47 kev-laptop kernel: [  717.905323] line6usb: Unknown symbol snd_ctl_add
    Sep 20 22:02:47 kev-laptop kernel: [  717.905379] line6usb: disagrees about version of symbol snd_pcm_new
    Sep 20 22:02:47 kev-laptop kernel: [  717.905380] line6usb: Unknown symbol snd_pcm_new
    Sep 20 22:02:47 kev-laptop kernel: [  717.905439] line6usb: disagrees about version of symbol snd_card_register
    Sep 20 22:02:47 kev-laptop kernel: [  717.905440] line6usb: Unknown symbol snd_card_register
    Sep 20 22:02:47 kev-laptop kernel: [  717.905498] line6usb: disagrees about version of symbol snd_card_free
    Sep 20 22:02:47 kev-laptop kernel: [  717.905499] line6usb: Unknown symbol snd_card_free
    Sep 20 22:02:47 kev-laptop kernel: [  717.905557] line6usb: disagrees about version of symbol snd_pcm_lib_preallocate_pages_for_all
    Sep 20 22:02:47 kev-laptop kernel: [  717.905559] line6usb: Unknown symbol snd_pcm_lib_preallocate_pages_for_all
    Sep 20 22:02:47 kev-laptop kernel: [  717.905667] line6usb: disagrees about version of symbol snd_pcm_stop
    Sep 20 22:02:47 kev-laptop kernel: [  717.905668] line6usb: Unknown symbol snd_pcm_stop
    Sep 20 22:02:47 kev-laptop kernel: [  717.905917] line6usb: disagrees about version of symbol snd_ctl_new1
    Sep 20 22:02:47 kev-laptop kernel: [  717.905918] line6usb: Unknown symbol snd_ctl_new1
    Sep 20 22:02:47 kev-laptop kernel: [  717.906043] line6usb: Unknown symbol snd_rawmidi_transmit_ack
    Sep 20 22:02:47 kev-laptop kernel: [  717.906261] line6usb: disagrees about version of symbol snd_pcm_hw_constraint_ratdens
    Sep 20 22:02:47 kev-laptop kernel: [  717.906262] line6usb: Unknown symbol snd_pcm_hw_constraint_ratdens
    Sep 20 22:02:47 kev-laptop kernel: [  717.906379] line6usb: disagrees about version of symbol snd_pcm_lib_malloc_pages
    Sep 20 22:02:47 kev-laptop kernel: [  717.906381] line6usb: Unknown symbol snd_pcm_lib_malloc_pages
    Sep 20 22:02:47 kev-laptop kernel: [  717.906437] line6usb: disagrees about version of symbol snd_pcm_lib_ioctl
    Sep 20 22:02:47 kev-laptop kernel: [  717.906439] line6usb: Unknown symbol snd_pcm_lib_ioctl
    Sep 20 22:02:47 kev-laptop kernel: [  717.906546] line6usb: disagrees about version of symbol snd_pcm_lib_free_pages
    Sep 20 22:02:47 kev-laptop kernel: [  717.906547] line6usb: Unknown symbol snd_pcm_lib_free_pages
    Sep 20 22:02:47 kev-laptop kernel: [  717.906617] line6usb: Unknown symbol snd_rawmidi_transmit_peek
    Sep 20 22:02:47 kev-laptop kernel: [  717.906771] line6usb: disagrees about version of symbol snd_pcm_set_ops
    Sep 20 22:02:47 kev-laptop kernel: [  717.906773] line6usb: Unknown symbol snd_pcm_set_ops
    Sep 20 22:02:47 kev-laptop kernel: [  717.906963] line6usb: disagrees about version of symbol snd_pcm_suspend_all
    Sep 20 22:02:47 kev-laptop kernel: [  717.906965] line6usb: Unknown symbol snd_pcm_suspend_all
    Sep 20 22:02:47 kev-laptop kernel: [  717.907035] line6usb: Unknown symbol snd_rawmidi_new
    Sep 20 22:02:47 kev-laptop kernel: [  717.907095] line6usb: disagrees about version of symbol snd_card_disconnect
    Sep 20 22:02:47 kev-laptop kernel: [  717.907097] line6usb: Unknown symbol snd_card_disconnect
    Sep 20 22:02:47 kev-laptop kernel: [  717.907230] line6usb: Unknown symbol snd_rawmidi_set_ops
    Sep 20 22:02:47 kev-laptop kernel: [  717.907413] line6usb: disagrees about version of symbol snd_card_create
    Sep 20 22:02:47 kev-laptop kernel: [  717.907414] line6usb: Unknown symbol snd_card_create
    Sep 20 22:02:47 kev-laptop kernel: [  717.907474] line6usb: disagrees about version of symbol snd_pcm_period_elapsed
    Sep 20 22:02:47 kev-laptop kernel: [  717.907475] line6usb: Unknown symbol snd_pcm_period_elapsed

Against my will, and to not waste time, I resigned myself to use a Windows machine lying around the office. I installed [Audacity](http://audacity.sourceforge.net) and the Windows drivers, then plugged the pod. And voilà, I had a portable recording studio.

Again, as we were in a hurry, we didn't paid close attention to the way Arnaud was speaking in the mic. Thus the quality of the original take was not fantastic. To me it was good enough for the intended purpose.

When I gave the raw recording to [Thomas](http://coolcavemen.com/biography/jimy-wong/) for mixing, he didn't take long for him to realize how bad we were at recording! Even without knowing how we proceed to record and what the setup looked like, he pointed out all the stuff we did wrong. I know him for a long time now, but he still amaze me with his technical and practical knowledge about audio stuff. I really want to thanks him for his help on this project!

![](/uploads/2010/tom-at-work-in-sound-up-studio.png)

By the way, if you're looking to record/mix/master any audio material (from a simple voice-over to a full band), I really recommend you to [contact his studio](http://soundupstudio.com). And tell him you heard of him by reading my blog, he may give you a discount! ;)

## Epilogue

As I concentrated all my efforts towards the creation of the video, I don't have many details about the application development itself. But coding the android app was, without a doubt, the biggest chunk of work of this project. It involves two of our best Andoid developpers (Jeremy and Paul) and [our in-house Photoshop geek](http://tilap.net) for the design. The project was lead by [Arnaud](http://www.infinityperl.org).

The whole project was completed in no time and virtually no budget thanks to the dedication and effort of Uperto's staff. Everybody in Uperto, from management to developpers, was fantastic. It really makes this team unique.

This project was a great oportunity for me to test my video skills. In a sense, it was my first professionnal assignment: I had a limited time, an inflexible deadline and a clear goal. But still, this type of activity falls into my hobby category. I have so much things to learn...

This project is also the first time I edit 1080p footage from my 7D in Kdenlive. This doesn't mean it's the first time I shoot with my 7D. In fact I shoot videos in various formats and setup for about a year. But my shooting skills only starts to be acceptable. My other projects involving 7D footages are currently on hold for various reasons (mostly more important stuff to do). That's why I hadn't published anything on the web since then. But I expect this situation to change soon! :D
