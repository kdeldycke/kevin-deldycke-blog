---
date: '2011-12-13'
title: WordPress commands
category: English
tags: Blog, MySQL, SQL, PHP, WordPress
---

- To activate the debug mode of WordPress, add the following PHP code in `wp-config.php`:

  ```php
  define('WP_DEBUG', true);
  ```

- This SQL query remove all revisions of posts having the `topic`, `reply` and `attachment` type (tested on WordPress 3.1.x):

  ```mysql
  DELETE child.*
  FROM wp_posts AS child
  LEFT JOIN wp_posts AS parent ON parent.ID = child.post_parent
  WHERE child.post_type = "revision" AND parent.post_type IN ("topic", "reply", "attachment");
  ```

- Count the number of posts, pages, revisions and comments produced by each user:

  ```mysql
  SELECT COUNT(u.ID) AS content_per_user, user_nicename, u.ID AS user_id
  FROM wp_users AS u
  LEFT JOIN wp_posts AS p ON p.post_author = u.ID
  LEFT JOIN wp_comments AS c ON c.user_id = u.ID
  GROUP BY u.ID;
  ```
