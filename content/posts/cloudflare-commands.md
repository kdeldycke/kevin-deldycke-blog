---
date: 2022-06-10 12:00
title: CloudFlare commands
category: English
tags: cloud, cloud computing, saas, iaas, paas, development, CLI, dns, cloudflare,
  API
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
