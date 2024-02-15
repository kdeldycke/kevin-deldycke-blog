---
date: '2006-12-20'
title: Image Processing commands
category: English
tags: CLI, EXIF, image, imagemagick, JPEG, Linux, Metadata, mogrify, pngcrush, mozjpeg
---

## Conversion

- Convert several files from a format to another:

  ```shell-session
  $ convert img_*.bmp img_%04d.png
  ```

## Resize

- Resize images of the current folder to progressive jpeg. Resized images will not be greater than 600x600, but the aspect ratio will be respected:

  ```shell-session
  $ convert -resize 600x600 -sharpen 1 -interlace Line ./* ./pict%04d.jpg
  ```

- Reduce size of a PDF by limiting its images to 1000 pixels and convert its color-space to grayscale:

  ```shell-session
  $ convert -resize 1000x1000 -type Grayscale ./big.pdf ./smaller.pdf
  ```

- Assemble images vertically:

  ```shell-session
  $ convert img1.jpg img2.jpg img3.jpg -append big.jpg
  ```

- Assemble images horizontally:

  ```shell-session
  $ convert img1.jpg img2.jpg img3.jpg +append big.jpg
  ```

## Cropping

- Remove all whitespace (or any solid-color) surrounding the `original.png` image:

  ```shell-session
  $ convert ./original.png -trim ./trimmed.png
  ```

- Add a 5% white border around the image:

  ```shell-session
  $ convert ./original.png -bordercolor White -border 5%x5% ./original-with-border.png
  ```

- Same as above but with a deep black 5% border on the side and a total image height 3x times taller as the original:

  ```shell-session
  $ convert ./original.png -bordercolor '#1a1a1a' -border 5%x100% ./original-with-border.png
  ```

## Optimization

- Massive in-place optimization of all PNG images available in sub-directories:

  ```shell-session
  $ find ./ -iname "*.png" -exec pngcrush "{}" "{}.crushed" \; -exec mv "{}.crushed" "{}" \;
  ```

- Same as above, but remove all known chunks, those encoding color profiles, gamma and text, and only keeps transparency chunks:

  ```shell-session
  $ find ./ -iname "*.png" -exec pngcrush -rem alla "{}" "{}.crushed" \; -exec mv "{}.crushed" "{}" \;
  ```

- Lossless optimization of JPEG files:

  ```shell-session
  $ find . -iname "*.jpg" -exec jpegtran -optimize -outfile "{}.optimized.jpeg" "{}" \;
  ```

- Convert a PNG file to an optimized JPEG:

  ```shell-session
  $ convert ./original.png TGA:- | cjpeg -optimize -progressive -quality 80 -outfile compressed-image.jpeg -targa
  ```

- Same as above but as a loop for all PNG files in current folder:

  ```shell-session
  $ for f in *.png; do convert "$f" TGA:- | cjpeg -optimize -progressive -quality 80 -outfile "$f.jpeg" -targa; done
  ```

## Metadata

- Print all metadata of a video file:

  ```shell-session
  $ exiftool ./MVI_4441.MOV
  Audio Channels                  : 2
  Compressor Version              : CanonAVC0002
  Camera Model Name               : Canon EOS 7D
  Firmware Version                : Firmware Version 2.0.3
  Image Size                      : 1920x1080
  Megapixels                      : 2.1
  Avg Bitrate                     : 47.5 Mbps
  (...)
  ```

- Same as above but print the canonical ID of each field:

  ```shell-session
  $ exiftool -short ./MVI_4441.MOV
  AudioChannels                   : 2
  CompressorVersion               : CanonAVC0002
  Model                           : Canon EOS 7D
  FirmwareVersion                 : Firmware Version 2.0.3
  ImageSize                       : 1920x1080
  Megapixels                      : 2.1
  AvgBitrate                      : 47.5 Mbps
  (...)
  ```

- Print all metadata, with fields grouped by their family:

  ```shell-session
  $ exiftool -groupHeadings MVI_4586.MOV
  ---- ExifTool ----
  ExifTool Version Number         : 12.60
  ---- File ----
  File Name                       : MVI_4586.MOV
  File Type                       : MOV
  File Type Extension             : mov
  MIME Type                       : video/quicktime
  ---- QuickTime ----
  Major Brand                     : Apple QuickTime (.MOV/QT)
  Minor Version                   : 2007.9.0
  Media Data Offset               : 32
  Movie Header Version            : 0
  (...)
  ```

- Show all date fields with their canonical IDs, grouped by family:

  ```shell-session
  $ exiftool -groupNames -short -'*Date' MVI_4586.MOV
  [File]          FileModifyDate                  : 2023:06:03 17:14:28+04:00
  [File]          FileAccessDate                  : 2023:06:03 21:36:26+04:00
  [File]          FileInodeChangeDate             : 2023:06:03 18:55:28+04:00
  [QuickTime]     CreateDate                      : 2015:09:26 14:44:10
  [QuickTime]     ModifyDate                      : 2015:09:26 14:44:10
  [QuickTime]     TrackCreateDate                 : 2015:09:26 14:44:10
  [QuickTime]     TrackModifyDate                 : 2015:09:26 14:44:10
  [QuickTime]     MediaCreateDate                 : 2015:09:26 14:44:10
  [QuickTime]     MediaModifyDate                 : 2015:09:26 14:44:10
  ```

- Copy the `CreateDate` field of the `QuickTime` family from a `MVI_4586.MOV` file to `MVI_4586.mp4`:

  ```shell-session
  $ exiftool -tagsfromfile MVI_4586.MOV "-QuickTime:CreateDate" MVI_4586.mp4
  ```

- Same as above but for all date fields:

  ```shell-session
  $ exiftool -tagsfromfile MVI_4586.MOV "-QuickTime:*Date" MVI_4586.mp4
  ```

- Transfer all `*Date` fields from all `.MOV` files of the current `./` directory to their corresponding `.mp4` files:

  ```shell-session
  $ exiftool -tagsfromfile %f.MOV "-QuickTime:*Date" -ext mp4 ./
  ```

- Remove all metadata of a JPEG file:

  ```shell-session
  $ exiftool -all= image.jpg
  ```

- Prefix all JPEG filename with their EXIF date:

  ```shell-session
  $ for i in *.jpg; do exiv2 -v -r '%Y%m%d_%H%M%S_:basename:' rename "$i"; done
  ```

- Remove recursively (and in-place) the color profile and comments embedded in all PNG images:

  ```shell-session
  $ mogrify -verbose -monitor -strip ./*.png
  ```

## macOS's Photos.app & `osxphotos`

- Export all videos from the `2012-12-32 - NYE` album to the current folder, and download from iCloud the missing ones:

  ```shell-session
  $ osxphotos export ./ --album "2012-12-32 - NYE" --download-missing --only-movies
  ```

- Same as above but only for videos shot with a Canon camera and encoded with the `CanonAVC0002` codec:

  ```shell-session
  $ osxphotos export ./ --album "2012-12-32 - NYE" --download-missing --only-movies --exif CompressorVersion 'CanonAVC0002'
  ```

- Export all videos from the `Yearly archives/2014` subfolder while keeping the same folder structure:

  ```shell-session
  $ osxphotos export ./ --regex "Yearly archives/2014" "{folder_album}" --download-missing --only-movies --directory "{folder_album}"
  ```
