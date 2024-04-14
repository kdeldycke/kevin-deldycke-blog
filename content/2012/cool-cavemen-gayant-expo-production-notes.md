---
date: '2012-11-06'
title: 'Cool Cavemen at Gayant Expo: production notes'
Category: Front Page
tags: band, concert, Cool Cavemen, Douai, France, gayant expo, Kdenlive, Stage Lighting, live, SoundUp studio, Video, YouTube
---

I've just realized I've never really finished the
[series of posts]({tag}gayant-expo) I
[started in 2010]({filename}/2010/cool-cavemen-live-gayant-expo-first-video-released.md),
a series about my longest video project: the
[biggest concert](https://coolcavemen.com/2009/concert-a-gayant-expo-les-photos/)
we performed with [Cool Cavemen](https://coolcavemen.com) in 2009.

![]({attach}gayant-expo-live-preview.jpg)

Cool Cavemen is
[working right now on a new album](https://coolcavemen.com/2011/le-grand-retour/),
which means we're approaching the end of the
[Multipolar](https://coolcavemen.bandcamp.com/album/multipolar)-era. This is the
right time to dig out what is, without a doubt, the video condensing all the
spirit and intensity of the period. Look at those dancing people! Look how they
like our music! Look how musicians have fun on stage! :)

https://www.youtube.com/watch?v=qE-bis-wYxs&list;=SP4BAA557B7144031F

By gathering all kinds of footage from the event, I was able to generate this
1-hour coverage of the concert. It took me the whole year of 2010 to edit and
publish it, one song at a time. This delay was mostly due to lacks of time, an
[unstable MacBook]({filename}/2009/macosx-is-irritating.md#update-may-2010)
and numerous Kdenlive crashes, all of these forcing me to re-create and redo my
projects from scratch several times (_sigh_).

## Lighting Design

I not only edited this video. I also was in charge of the
[stage lighting design](https://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=Stage%20Lighting%20Design&linkCode=ur2&rh=i%3Aaps%2Ck%3AStage%20Lighting%20Design&tag=kevideld-20&url=search-alias%3Daps)
of the concert:

![](https://www.assoc-amazon.com/e/ir?t=kevideld-20&l=ur2&o=1)

![working-on-grand-ma-001]({attach}working-on-grand-ma-001.jpg)

![working-on-grand-ma-002]({attach}working-on-grand-ma-002.jpg)

![working-on-grand-ma-003]({attach}working-on-grand-ma-003.jpg)

It was the first time I had so much gear to work with (mostly
[Martin Mac-2000](https://www.martin.com/product/product.asp?product=mac2000profile)
and [Mac-700](https://martin.com/product/product.asp?product=mac700profile)),
including the full-size version of the
[Grand-MA v1 lighting console](https://en.audiofanzine.com/automatic-lighting-console/ma-lighting/GrandMA-Fullsize/).
A week before the show, I played with
[GrandMA's emulator](https://www.malighting.com/en/products/control/grandma-onpc.html)
to get a glimpse of that desk's philosophy.

![]({attach}grand-ma-onpc-simulation.png)

But this little training is not enough to get used to the GrandMA, let alone
master it. So when it was time to play live, I choose simple lighting patterns
and movements. Of course I made a lots of mistakes and the result was far from
perfect, but it was good enough to keep the show running. Considering these
conditions, my performance was a success! :)

And I had a secret weapon: I knew I'll be the one editing the video. Being both
the lighting designer and the video editor, I was able to hide all the things
that didn't fell right, and fix all the timing issue after the facts.

## Synchronization

The audio is a multitrack recording taken directly from the
[front of house](https://en.wikipedia.org/wiki/Front_of_House) mixing console,
and saved on a
[MacBook](https://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=apple%20macbook&linkCode=ur2&rh=i%3Aaps%2Ck%3Aapple%20macbook&tag=kevideld-20&url=search-alias%3Daps):

![](https://www.assoc-amazon.com/e/ir?t=kevideld-20&l=ur2&o=1)

![IMG_0492]({attach}IMG_0492.jpg)

![IMG_0502]({attach}IMG_0502.jpg)

![p1010733]({attach}p1010733.jpg)

The raw recording was later remixed by Thomas of the
[SoundUp Studio](https://soundupstudio.com/).

Using different software for audio and video editing, proved to be challenging.
And we were worried about the effect of bad synchronization. After some
research, it looks like humans tolerate an error below 100ms:

<blockquote>
  <p>100 ms being the limit under which the temporal gap between audio and video
  cannot be noticed.</p>
  <small>Philippe Owezarski (LAAS-CNRS), <cite title="Enforcing Multipoint
  Multimedia Synchronisation in Videoconferencing Applications"><a
  href="https://books.google.fr/books?id=3IdKbKOxZL4C&amp;pg=PA69&amp;lpg=PA69">
  Enforcing Multipoint Multimedia Synchronisation in Videoconferencing
  Applications</a></cite></small>
</blockquote>

Now that we have our error margin, we need a workflow. We managed to design one
based on a reference track extracted from the camera recording:

1. First, Thomas start to work on a song. When he has something to show us, he
   down-mix its
   [Cubase](https://www.amazon.com/s/?_encoding=UTF8&camp=1789&creative=390957&field-keywords=Steinberg%20Cubase&linkCode=ur2&rh=i%3Aaps%2Ck%3ASteinberg%20Cubase&tag=kevideld-20&url=search-alias%3Daps)
   project and export intermediate results under the name
   `2010-01-29--igor--audio-desync.wav`. This allow all band members to give
   feedback.

![](https://www.assoc-amazon.com/e/ir?t=kevideld-20&l=ur2&o=1)

2. Once the final mix of the song is validated, I export the audio reference
   from my video edit (i.e. the plain recording from the cameras) under the
   name `2010-02-15--igor--audio-ref.wav`. We use this file as the reference
   audio track.

1. Then, Thomas shift in time the `2010-01-29--igor--audio-desync.wav` file to
   precisely match the `2010-02-15--igor--audio-ref.wav` reference file, and
   save the result under the name `2010-02-16--igor--audio-sync.wav`. This is
   the file I import in Kdenlive and align with my video using the reference
   track.

![]({attach}kdenlive-fusion-timeline.png)

Before using that workflow on all our tracks, we checked it was not introducing
delays. Unfortunately, I detected some:

![export-PTFU-audio-ref]({attach}export-PTFU-audio-ref.png)

![export-PTFU-master]({attach}export-PTFU-master.png)

I introduced them when I tried to
[get rid of video timecode artifacts]({filename}/2010/remove-videotape-timecode.md).
I messed with encoding parameters in Avidemux, and introduced delays. When I
realized I could just use the crop filter in Kdenlive, instead of removing the
timecode in an external software, I produced perfect timing. That's another big
lesson of that project: stay in Kdenlive.
