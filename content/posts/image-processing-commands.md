comments: true
date: 2006-12-20 20:42:35
layout: post
slug: image-processing-commands
title: Image Processing commands
wordpress_id: 121
category: English
tags: CLI, exiftool, image, imagemagick, JPEG, Linux, Metadata, mogrify, photo, picture, pngcrush

  * Convert several files from a format to another:

        :::console
        convert img_*.bmp img_%04d.png

  * Resize images of the current folder to progressive jpeg. Resized images will not be greater than 600x600, but the aspect ratio will be respected:

        :::console
        convert -resize 600x600 -sharpen 1 -interlace Line * pict%04d.jpg

  * Remove all metadata of a JPEG file:

        :::console
        exiftool -all= image.jpg

  * Remove recursively (and in-place) the color profile and comments embedded in all PNG images:

        :::console
        mogrify -verbose -monitor -strip ./*.png

  * Massive in-place optimization of all PNG images available in sub-directories:

        :::console
        find ./ -iname "*.png" -exec pngcrush "{}" "{}.crushed" \; -exec mv "{}.crushed" "{}" \;

  * Same as above, but remove all known chunks, those encoding color profiles, gamma and text, and only keeps transparency chunks:

        :::console
        find ./ -iname "*.png" -exec pngcrush -rem alla "{}" "{}.crushed" \; -exec mv "{}.crushed" "{}" \;

  * Lossless optimization of JPEG files:

        :::console
        find . -iname "*.jpg" -exec jpegtran -optimize -outfile "{}.optimized.jpeg" "{}" \;

