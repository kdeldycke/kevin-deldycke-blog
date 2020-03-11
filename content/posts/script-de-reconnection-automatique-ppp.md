---
date: 2005-04-04 00:07:45
title: Script de reconnection automatique PPP
category: Français
tags: Linux, Network, Script, shell, cron
---

Voici un petit script trivial en bash qui, couplé à `cron`, me permet de maintenir ma connexion internet 56kbps fournie par Free.fr (en attendant l'arrivée du modem ADSL):

    :::shell-session
    #!/bin/bash
    # Script de reconnection automatique

    testconnect() {
      CONNECT=`ping -c 3 google.com | grep packets | cut -d' ' -f4`
    }

    doconnect() {
      logger -t reconnect Essai reconnection.
      /etc/init.d/internet restart
    }

    displayip() {
      IP=`/sbin/ifconfig | grep -A 1 ppp0 | grep inet | cut -d' ' -f12 | cut -d':' -f2`
      logger -t reconnect Adresse IP : "$IP"
    }

    logger -t reconnect Test connection.
    testconnect
    if [ "$CONNECT" = "0" ];
      then
        logger -t reconnect Connection perdue.
        doconnect
        testconnect
        if [ "$CONNECT" != "0" ];
          then
            logger -t reconnect Reconnection OK.
            displayip
          else
            logger -t reconnect Reconnection manquee.
        fi
      else
        logger -t reconnect Connection OK.
        displayip
    fi

    exit 0
    # FIN

