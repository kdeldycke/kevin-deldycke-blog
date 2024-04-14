---
date: '2022-06-10'
title: CloudFlare commands
category: English
tags: cloud, cloud computing, saas, iaas, paas, development, CLI, dns, cloudflare, API
---

## DNS records

- List DNS records of a zone:

  ```shell-session
  $ curl -X GET "https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/dns_records" \
      -H "Authorization: Bearer <TOKEN>" \
      -H "Content-Type:application/json"
  ```

- List DNS records IDs of a zone:

  ```shell-session
  $ curl -X GET "https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/dns_records" \
      -H "Authorization: Bearer <TOKEN>" \
      -H "Content-Type:application/json" \
      | jq '.result[].id'
  "82c881261189dc8b8ddbd756cffccd21"
  "324437ed3e1212770edeabb65bb3cd6a"
  ```

- Delete one DNS record:

  ```shell-session
  $ curl -X DELETE "https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/dns_records/<RECORD_ID>" \
      -H "Authorization: Bearer <TOKEN>" \
      -H "Content-Type:application/json"
  ```

- Delete all DNS records of a zone:

  ```shell-session
  $ curl -X GET "https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/dns_records" \
      -H "Authorization: Bearer <TOKEN>" \
      -H "Content-Type:application/json" \
      | jq --raw-output '.result[].id' \
      | xargs -I '{}' \
      curl -X DELETE "https://api.cloudflare.com/client/v4/zones/<ZONE_ID>/dns_records/{}" \
          -H "Authorization: Bearer <TOKEN>" \
          -H "Content-Type:application/json"
  ```

## Redirects

CloudFlare have several redirection options:

- [Pages redirects](https://developers.cloudflare.com/pages/platform/redirects/): for static sites hosted on CloudFlare, via a `_redirects` file.
- [Page Rules](https://support.cloudflare.com/hc/en-us/articles/200172286-Configuring-URL-forwarding-or-redirects-with-Cloudflare-Page-Rules)

### Pages redirects

This blog uses [CloudFlare Pages](https://pages.cloudflare.com/) to host all its static content. To redirect old URLs to new ones, I use a [`_redirects` file at the root of the repository](https://github.com/kdeldycke/kevin-deldycke-blog/blob/main/content/extra/_redirects). You should inspect that file to see how it works.

Note that this kind of redirects are not working at the domain-level. If you want to redirect `https://example.com/` to `https://www.example.com/`, you need to use [Page Rules](#page-rules).

Here are some of the most useful rules:

- By default, [pages are redirected for normalization](https://developers.cloudflare.com/pages/platform/serving-pages/#route-matching):

  | From                | To         |
  | ------------------- | ---------- |
  | `/contact`          | `/contact` |
  | `/contact/`         | `/contact` |
  | `/contact.html`     | `/contact` |
  | `/about`            | `/about/`  |
  | `/about/`           | `/about/`  |
  | `/about/index.html` | `/about/`  |

  Note how folder roots with an `index.html` are always redirected to an URL with a trailing slash, while HTML files are stripped of their extension.

  This behavior cannot be changed.

- Redirect a single URL:

  ```text
  /old-url /new-url 301
  ```

- Redirect empty folders to the root of the site:

  ```text
  /empty-folder      /   301
  /empty-folder/     /   301
  ```

  I use this double rule to catch both the folder named `empty-folder`, and an hypothetical file named `empty-folder.html`. That way I am sure a parasitic `empty-folder.html` won't be served.

## Page rules

`TODO`
