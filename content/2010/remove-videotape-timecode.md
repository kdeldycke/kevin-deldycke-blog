---
date: '2010-01-14'
title: Remove videotape timecode
category: English
tags: analog, avidemux, timecode, Video, VITC
---

Since November I'm working on a video project with footages taken with an
analog system. This mean that some videos were shots with analog cameras,
recorded on a videotape, then transcoded to a MPEG-2 stream.

Because of the analog nature of the filming process' first steps (on which I
had no control), I ended up with some artefacts:

![]({attach}analog-videotape-timecode.png)

See? No? Here is an upscaled version:

![]({attach}analog-videotape-timecode-upscaled-detail.png)

Yes, that's it: there is white dots on top of each frame.

I discovered that these dots represents a [binary timecode
](https://documentation.apple.com/en/finalcutpro/usermanual/chapter_D_section_7.html#apple_ref:doc:uid:TempBookID-ReplacedWhenAssociatingWithMessierRevision-44035FRT-1001444)
called the [Vertical Interval TimeCode, or VITC
](https://en.wikipedia.org/wiki/Vertical_interval_timecode). In the old days of
analog video, some timecodes were directly embedded in video or audio signals.
Nowadays, in this all-digital world, timecodes are saved as metadata in video
files.

So we are left with these deprecated and ugly white dots... For aesthetical
reasons, I wanted to remove them. To do this job, I used [Avidemux
](https://avidemux.berlios.de), an open source free software available on all
majors platforms (Windows, Mac OS X and Linux).

The removal process is really straightforward: I've just added a black
rectangle over these dots to hide them. Here is how to do it:

1. Open your original file in Avidemux;

1. Click on the `Filters` button;

1. Go to `Transform`, then `Blacken Borders` and click on the `+` button;

1. Use the dialog to set a 2 pixels top border;

1. Now you have to export the result using a reasonable video codec, and
   that's it!

![]({attach}avidemux-add-black-border.png)
