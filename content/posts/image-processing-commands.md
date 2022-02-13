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
        $ convert -resize 600x600 -sharpen 1 -interlace Line ./* ./pict%04d.jpg
        ```

  * Reduce size of a PDF by limiting its images to 1000 pixels and convert its color-space to grayscale:

        ```shell-session
        $ convert -resize 1000x1000 -type Grayscale ./big.pdf ./smaller.pdf
        ```
  
  * Assemble images vertically:

        ```shell-session
        $ convert img1.jpg img2.jpg img3.jpg -append big.jpg
        ```
        
  * Assemble images horizontally:

        ```shell-session
        $ convert img1.jpg img2.jpg img3.jpg +append big.jpg
        ```

## Cropping

  * Remove all whitespace (or any solid-color) surrounding the `original.png` image:

        ```shell-session
        $ convert ./original.png -trim ./trimmed.png
        ```

  * Add a 5% white border around the image:

        ```shell-session
        $ convert ./original.png -bordercolor White -border 5%x5% ./original-with-border.png
        ```

  * Same as above but with a deep black 5% border on the side and a total image height 3x times taller as the original:

        ```shell-session
        $ convert ./original.png -bordercolor '#1a1a1a' -border 5%x100% ./original-with-border.png
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
        $ convert ./original.png TGA:- | cjpeg -optimize -progressive -quality 80 -outfile compressed-image.jpeg -targa
        ```

  * Same as above but as a loop for all PNG files in current folder:

        ```shell-session
        $ for f in *.png; do convert "$f" TGA:- | cjpeg -optimize -progressive -quality 80 -outfile "$f.jpeg" -targa; done
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
