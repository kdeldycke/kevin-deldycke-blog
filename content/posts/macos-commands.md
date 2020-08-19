---
date: 2019-07-22 23:18:55
title: macOS commands
category: English
tags: CLI, macOS, Apple, OSX, PluginKit
---

  * List available PluginKit extensions:

        ```shell-session
        $ pluginkit -mAvvv
        ```

  * Get infos on a PluginKit extensions:

        ```shell-session
        $ pluginkit -m -v -i com.agilebits.onepassword7.1PasswordSafariAppExtension
        ```

  * Enable a PluginKit extensions:

        ```shell-session
        $ pluginkit -e use -i com.agilebits.onepassword7.1PasswordSafariAppExtension
        ```

  * [Install Steam in a case-insensitive disk image](https://github.com/kdeldycke/dotfiles/blob/b711023285488f94fa0968a5ceff75c4322548bd/scripts/osx-install.sh#L149-L162).
