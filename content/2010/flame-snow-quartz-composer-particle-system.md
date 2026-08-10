---
date: '2010-11-09'
title: Flame & Snow, using Quartz Composer particle system
category: English
tags: Animation, Apple, MacBook, QC Experiment, Quartz Composer, Video, Visual
---

After creating a [series of compositions]({filename}/2010/sharp-scan-lines-squared-lava-lamp.md) based on my [kaleidoscopic patch]({filename}/2010/kaleidoscope-001-002.md), I played with Quartz Composer's particle system, to create a flame and falling snow flakes:

https://www.youtube.com/watch?v=wsYLevXRytA

https://www.youtube.com/watch?v=0FH_-_chcfY

As for the last times, both [Flame]({attach}flame.qtz) and [Snow]({attach}snow.qtz) source compositions are available. Flame's patch looks like this:

![Quartz Composer flame patch: a Particles patch feeding an image crop, a motion blur and a second crop before reaching the billboard, with a gradient patch off to the side](flame-patch.png)

And here is Snow's patch preview:

![Quartz Composer snow patch: an image-with-string patch cropped and bloomed to make the flake texture, fed into a particle system whose position is driven by an LFO](snow-patch.png)
