---
date: '2010-07-28'
title: Exim commands
category: English
tags: CLI, email, Exim, Linux, Mail transfer agents
---

- List mails in the queue:

  ```shell-session
  $ exim -bp
  ```

- View headers of a mail:

  ```shell-session
  $ exim -Mvh <mail-id>
  ```

- View body of a mail:

  ```shell-session
  $ exim -Mvb <mail-id>
  ```

- Remove a mail from the queue:

  ```shell-session
  $ exim -Mrm <mail-id>
  ```

- Remove all frozen mails in the queue:

  ```shell-session
  $ exiqgrep -z -i | xargs exim -Mrm
  ```
