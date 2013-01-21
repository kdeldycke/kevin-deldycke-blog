comments: true
date: 2011-07-12 12:45:11
layout: post
slug: making-of-omashay-wish-you-looked-at-me-music-video
title: Making of Omashay's "Wish You Looked at Me" music video
wordpress_id: 3386
category: English
tags: 1080p, 720p, Cool Cavemen, editing, kdenlive, Linux, Music, music video, omashay, Video, youtube

Last month I edited the [Wish You Looked at Me video clip](http://omashay.com/wish-you-looked-at-me-video-clip/) for the [Omashay project](http://omashay.com). This is a side-project of [Cool Cavemen's saxophonist](http://coolcavemen.com/biography/tomasito/). The video is finally available on YouTube:

http://www.youtube.com/watch?v=iHi0lwhTqqc

[![](http://ws.assoc-amazon.com/widgets/q?_encoding=UTF8&Format=_SL110_&ASIN=B001SER45Q&MarketPlace=US&ID=AsinImage&WS=1&tag=kevideld-20&ServiceVersion=20070822)](http://www.amazon.com/gp/product/B001SER45Q/ref=as_li_tf_il?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399381&creativeASIN=B001SER45Q) All the video material was shot by Tomasito itself, with his [Canon PowerShot SX200IS](http://www.amazon.com/gp/product/B001SER45Q/ref=as_li_tf_tl?ie=UTF8&tag=kevideld-20&linkCode=as2&camp=217145&creative=399381&creativeASIN=B001SER45Q) point-and-shoot camera. This camera produce 30fps 720p clips.
![](http://www.assoc-amazon.com/e/ir?t=kevideld-20&l=as2&o=1&a=B001SER45Q&camp=217145&creative=399381)





He came to me with all these `.mov` files, and the idea of combining them into a classical split-screen layout. He had no idea how to do this, so I accepted to help him with my technical knowledge.

I fired up my Kdenlive (v0.8 on Kubuntu 11.04) and in a matter of hours, the project was done. With source videos of 720p, I naturally chose 1080p as the final resolution. I kept the 30fps framerate to not alter the original time resolution.

The most boring part of the edit was the first step, in which we synced all clips together with the reference audio track. Here is how the timeline looked, with one track for each instrument:

[![](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-01-300x187.png)](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-01.png)

We had to work around some annoying Kdenlive bugs, as it had some problems handling so much tracks in parallel. Fortunately these bugs were fixed in a matter of days with a new build of MLT.

Next step was to mark out the structure of the song. Tomasito placed blue markers along the timeline, and we cut all tracks following that structure. It resulted in a matrix of clips:

[![](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-02-300x187.png)](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-02.png)

Then for each segment, we choose the 4 clips that we wanted to show and deleted the others:

[![](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-04-300x187.png)](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-04.png)

Then I created 4 special tracks to which I applied a global positioning and scaling effect, to have each track fill one corner of the screen. We moved there all the clips we selected in the previous step, and cleaned up the timeline a bit:

[![](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-05-300x187.png)](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-05.png)

At this stage the project was mostly done. It was just a matter of adding intro, outro and fade in/out to obtain our final video:

[![](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-06-300x187.png)](http://kevin.deldycke.com/wp-content/uploads/2011/07/wish-you-looked-at-me-kdenlive-timeline-06.png)

Tomasito basically did the whole editing of the project. And I have some evidences:

[![](http://kevin.deldycke.com/wp-content/uploads/2011/07/tomasito-editing-session-300x200.jpg)](http://kevin.deldycke.com/wp-content/uploads/2011/07/tomasito-editing-session.jpg)

I just showed him how to manipulate Kdenlive timelines, and cut/move/paste clips, and he was absolutely autonomous in a matter of minutes. I just did the transitions, the title cards integration and the screen splitting. I'm not sure I deserve the title of editor for this project, but he still insisted to add me in the credits... :)

Of course split-screen is [far from new](http://monsterkidclassichorrorforum.yuku.com/reply/304973/Oldest-Split-Screen-effect#reply-304973) and [was done](http://www.youtube.com/watch?v=vsMIuuV05uc) [a million times before](http://en.wikipedia.org/wiki/Split_screen_(filmmaking)#List_of_notable_films_using_split_screen). But it's a simple yet effective concept that require absolutely no investment (apart time). This also gave me the opportunity to play again with Kdenlive and assess its user-friendliness and edit capabilities on a real project. But at the end, it was just a great excuse to work with a friend on a little video project ! :)
