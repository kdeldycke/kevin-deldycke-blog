---
date: 2006-12-20 20:42:35
title: Image Processing commands
category: English
tags: CLI, EXIF, image, imagemagick, JPEG, Linux, Metadata, mogrify, pngcrush, mozjpeg
---

## Conversion

  * Convert several files from a format to another:

        ```shell-session
        $ convert img_*.bmp img_%04d.png
        ```


## Resize

  * Resize images of the current folder to progressive jpeg. Resized images will not be greater than 600x600, but the aspect ratio will be respected:

        ```shell-session
        $ convert -resize 600x600 -sharpen 1 -interlace Line * pict%04d.jpg
        ```


## Cropping

  * Remove all whitespace (or any solid-color) surrounding the `original.png` image:

        ```shell-session
        $ convert ./original.png -trim ./trimmed.png
        ```

  * Add a 5% white border around the image:

        ```shell-session
        $ convert ./original.png -bordercolor White -border 5%x5% ./original-with-border.pmg
        ```


## Optimization

  * Massive in-place optimization of all PNG images available in sub-directories:

        ```shell-session
        $ find ./ -iname "*.png" -exec pngcrush "{}" "{}.crushed" \; -exec mv "{}.crushed" "{}" \;
        ```

  * Same as above, but remove all known chunks, those encoding color profiles, gamma and text, and only keeps transparency chunks:

        ```shell-session
        $ find ./ -iname "*.png" -exec pngcrush -rem alla "{}" "{}.crushed" \; -exec mv "{}.crushed" "{}" \;
        ```

  * Lossless optimization of JPEG files:

        ```shell-session
        $ find . -iname "*.jpg" -exec jpegtran -optimize -outfile "{}.optimized.jpeg" "{}" \;
        ```

  * Convert a PNG file to an optimized JPEG:

        ```shell-session
        $ convert ./original.png TGA:- | cjpeg -optimize -progressive -quality 70 -outfile compressed-image.jpg -targa
        ```


## Metadata

  * Remove all metadata of a JPEG file:

        ```shell-session
        $ exiftool -all= image.jpg
        ```

  * Prefix all JPEG filename with their EXIF date:

        ```shell-session
        $ for i in *.jpg; do exiv2 -v -r '%Y%m%d_%H%M%S_:basename:' rename "$i"; done
        ```

  * Remove recursively (and in-place) the color profile and comments embedded in all PNG images:

        ```shell-session
        $ mogrify -verbose -monitor -strip ./*.png
        ```
