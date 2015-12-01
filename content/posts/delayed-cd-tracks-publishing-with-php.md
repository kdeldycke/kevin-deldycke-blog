---
date: 2007-02-10 20:12:08
title: Delayed CD Tracks Publishing with PHP
category: English
tags: Cool Cavemen, Music, PHP, Web

Here is a little piece of code I want to share with you. I created this some months ago for the [Cool Cavemen band](http://coolcavemen.com). They wanted to release all tracks of their new LP on their website, one track per week. That's the main purpose of the code below:

    :::php
    <?php

    function renderTracks() {
      # Track list
      $track_list = array(
          "Track 1" => "cd-track-1"
        , "Track 2" => "cd-track-2"
        , "Track 3" => "cd-track-3"
        , "Track 4" => "cd-track-4"
        , "Track 5" => "cd-track-5"
        );
      # All variation of each track
      $track_format = array(
          ".mp3"  => "Mp3"
        , ".ogg"  => "Ogg/Vorbis"
        , ".flac" => "Flac"
        );
      # This is the list of all tracks which are always visible.
      $always_visible = array(1, 4);
      # Date and time when the "always_visible" tracks will be displayed.
      $start_date = mktime(18, 0, 0, 12, 1, 2006);
      # Delay between each track publication. Look at strtotime() manual for details.
      $delay = "+1 week";

      $today = mktime();
      $months = array(
           1 => "Janvier"
        ,  2 => "Février"
        ,  3 => "Mars"
        ,  4 => "Avril"
        ,  5 => "Mai"
        ,  6 => "Juin"
        ,  7 => "Juillet"
        ,  8 => "Août"
        ,  9 => "Septembre"
        , 10 => "Octobre"
        , 11 => "Novembre"
        , 12 => "Décembre"
      );

      # Compute publishing date of each track
      $track_dates = array();
      $track_number = 0;
      $track_publish_queue_order = 0;
      $previous_queue_date = $start_date;
      $new_start_date = $start_date;
      foreach($track_list as $track_title => $track_file) {
        $track_number++;
        # Is the track always published ?
        if (in_array($track_number, $always_visible)) {
          # Set publishing date to the start date
          $track_dates[$track_number] = $start_date;
        } else {
          # Compute the publishing date of the track
          $track_publish_queue_order++;
          $new_publishing_date = strtotime($delay, $previous_queue_date);
          $track_dates[$track_number] = $new_publishing_date;
          $previous_queue_date = $new_publishing_date;
        }
        # Update the start date of the period when a track is considered "new"
        if (($new_start_date <= $track_dates[$track_number]) and
            ($track_dates[$track_number] <= $today)) {
          $new_start_date = $track_dates[$track_number];
        }
      }
      # The end of the "new" track period is always today
      $new_stop_date = $today;

      # HTML rendering of each track
      $track_number     = 0;
      $html_published   = "<table>";
      $html_unpublished = $html_published;
      foreach($track_list as $track_title => $track_file) {
        $track_number++;
        $new          = False;
        $published    = False;
        $track_date   = $track_dates[$track_number];
        $track_html   = '';
        $publish_date = '';
        # Is the track published ?
        if ($track_dates[$track_number] < $today) {
          $published = True;
        }
        # Is the track new ?
        if (($new_start_date <= $track_date) and
            ($track_date <= $new_stop_date)) {
          $new = True;
        }
        if ($new) {
          $track_html .= '<tr><td><b>NEW!</b> </td><td>';
        } else {
          $track_html .= '<tr><td></td><td>';
        }
        # Create a direct download link for each track format
        if ($published) {
          foreach($track_format as $format_ext => $format_name) {
            $track_html .= sprintf( '<a href="http://coolcavemen.com/%s%s">'
                                  , $track_file
                                  , $format_ext
                                  );
            $track_html .= sprintf('%s</a> ', $format_name);
          }
        }
        if (! $published) $track_html .= '<span class="disabled">';
        $track_html .= '&mdash; ';
        # Show track as non-available, and print its release date
        if (! $published)
          $track_html .= sprintf( '<b>%s %s, %sh &raquo;</b> '
                                , date("j", $track_date)
                                , $months[(int) date("n", $track_date)]
                                , date("H", $track_date)
                                );
        $track_html .= sprintf('%s<br/>', $track_title);
        if (! $published) $track_html .= '</span>';
        $track_html .= '</td></tr>';
        if ($published) {
          $html_published .= $track_html;
        } else {
          $html_unpublished .= $track_html;
        }
      }
      return $html_published.'</table><hr/>'.$html_unpublished.'</table>';
    }

    ?>

Of course this code doesn't prevent someone to download the track if this person knows the exact URL. But having a bullet-proof system was not my priority: I had, at that time, to do something the quick and dirty way. So I give you this code as is it, without further explanations. This code is easy enough to let any rookie understand how it work.

Here is the final result, from the user point of view (and with additional aesthetic enhancements):

![cd-track-delayed-publishing](/uploads/2007/cd-track-delayed-publishing.png)

