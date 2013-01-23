comments: true
date: 2004-06-29 18:54:50
layout: post
slug: mise-en-place-paserelle-adsl-mandrake-10
title: Mise en place d'une paserelle ADSL sous Mandrake 10
wordpress_id: 4878
category: Français
tags: adsl, gateway, internet, Linux, Mandrake, Network, router

Voici un long article regroupant toutes mes notes sur mon projet de mise en place d'une passerelle internet tournant sous Linux.

Tout commence avec une épave de PC récupéré, composé de:

  * un écran
  * une carte graphique Matrox PCI G200
  * un bloc d'alimentation
  * un disque dur IDE de 6 Go
  * 128 Mo + 32 Mo de SD-RAM PC66
  * un processeur AMD K6 à 200Mhz
  * un lecteur CD-ROM IDE 52x
  * deux cartes réseaux ISA 3Com 3c509-b 10Mb avec RJ45
  * une clavier
  * une souris

Le tout repose sur une carte-mère sans nom et monté dans une carcasse de châssis de type "tour".

Les cartes réseaux ISA sont spéciales car elles nécessites une pré-configuration des IRQ et plages d'adressage. Cela se fait via un utilitaire de configuration MS-DOS fourni par 3Com. Après avoir mis ce programme sur disquette, j'ai ajouté temporairement un lecteur de disquettes à la machine le temps de configurer les cartes ISA.

On grave ensuite le premier CD de la Mandrake 10 official. On l’insère dans le lecteur, et on boot normalement. Si ça boot pas, vérifier que le bios est configuré pour démarrer sur le CD-ROM en premier, avant le disque dur.

On passe sans problème les premiers écrans de l'installation, et après avoir sélectionné la langue, accepté la licence GPL, choisi le type de clavier, on a à choisir le niveau de sécurité. On va le laisser sur standard. En fait nous n'allons jamais utiliser la configuration et les assistant de Mandrake.

Ensuite pour la partition, on prend 500 Mo pour `/`, 256 Mo pour le swap, et le reste pour `/home`. Toutes les partitions seront de type `ext3` car d’expérience ce format est plus tolérant aux coupures de courant. Une fois les partitions créée vient l'étape de sélection des packages.

Ne sélectionnez rien et décochez toute les cases de toutes les rubriques. Dé-sélectionner aussi la case "sélection individuelle des packages". Le programme d'installation va alors nous donner trois choix. Nous n'en sélectionnerons aucun parmi les trois car nous n'avons pas besoin de serveur X graphique, mais nous avons besoins de `urpmi` pour nous faciliter la vie. La documentation n'est pas nécessaire: ne l'installer pas. Cela nous fera économiser de la place sur le disque dur.

Les paquets de la Mandrake vont ensuite être installés depuis le CD-ROM.

Viens l'étape du choix du mot de passe `root`. Ne vous gênez pas pour une phrase complète (plus de 20 caractères) et mixez les chiffres, la casse et les ponctuations. Il est indispensable d'avoir un mot de passe compliqué car votre machine sera connecté 24/24 sur le net.

Ne créons pas d'autre utilisateurs pour le moment. On en rajoutera plus tard (voir même pas du tout).

Choisissons ensuite d'installer `grub` sur le MBR.

Vient ensuite la configuration de différents paramètres. Par défaut la config doit être ok. Mais nous allons changer deux trois bricoles.

Réglez l'horloge pour en vous déclarant dans le fuseau horaire UTC. Il faut ensuite spécifier que l'horloge du bios est sur GMT et que vous souhaitez synchroniser l'horloge automatiquement (via NTP). Utilisez le serveur NTP par défaut ou choisissez-en un qui se trouve dans votre pays ou zone géographique.

Nous allons maintenant changer la configuration du programme d'amorçage `grub`. Réglons le délai d'activation à une seconde, car notre machine est une machine dédiée sur laquelle ne tournera que Linux. Dans "avancé" on demandera de vider `/tmp` à chaque démarrage. Les entrées de la liste de boot seront conservée par défaut. On éditera ensuite chaque ligne pour spécifier via le menu "avancé" un mode de démarrage en 1024x768 (ou plus, ou moins) pour un plus grand confort en cas d'utilisation d'un écran.

Configurons ensuite les services. Nous ne garderons que les services `atd`, `crond`, `harddrake`, `keytable`, `network`, `syslog` et `random` pour le système. Nous ne sélectionnerons rien dans les services "autres", ni dans les autres catégories de services.

On ne téléchargera pas de mises à jour depuis le net, car notre PC est pour le moment isolé.

Il est temps de redémarrer l’ordinateur, sans oublier de retirer le CD du lecteur. Ce premier démarrage va nous permettre de vérifier que le système est capable de se lancer automatiquement dans une configuration minimale. Si vous obtenez une invite de login, vous avez gagné ! Vous avez un système qui démarre avec le minimum à bord !

Connectez vous avec le login `root` et le mot de passe définit précédemment.

Nous allons apprendre a installer avec `urpmi`. Installons `drakconf` (le panneau de config de Mandrake). Il ne nous servira que pour la configuration des interfaces réseau. Nous configurerons la sécurité avec `webmin`. On lance la commande:

    :::bash
    $ urpmi drakconf

`urpmi` va chercher les dépendances indispensable à `drakconf` pour fonctionner. Il va les lister et vous demander si vous voulez les installer. Répondez par l'affirmative, et insérez le CD n°1 quand il vous le demande. Il va ensuite installer sous vos yeux tout les packages nécessaires.

On lance ensuite `drakconf` en ligne de commande puis:

  * On entre dans le menu "network & internet".
  * Choisissez "connexion via LAN".
  * Il vous demandera éventuellement de choisir le driver de la carte manuellement si il ne peut le déterminer automatiquement. De même pour les paramètres du module/driver utilisé.
  * Choisissez ensuite de configurer `eth0`.
  * Puis demander une configuration de l'adresse IP manuelle, et non via le service `dhcp`. L'adresse IP sera `192.168.1.1/255.255.255.0` et la carte sera branchée à chaud sur le réseau et sera lancée au démarrage.
  * Ne changez pas la config dans l’écran suivant. Ni dans celui d’après (zeroconf).
  * Redémarrez enfin le réseau quand cela vous sera demandé.

Nous allons maintenant vérifier que le réseau est parfaitement configuré. Faite un `ifconfig`. Normalement vous devez avoir trois interfaces: `eth1`, `lo` et `eth0`.

Ensuite nous allons utiliser `drakconf` pour configurer la connexion internet. Toujours dans le menu "network & internet", on choisira une connexion par ADSL, via l'interface `eth1` quand on nous le demandera. Choisissons `pppoe` (`oe` pour "over ethernet"). Puis dans l’écran suivant, nous remplirons le formulaire des paramètres donnés par votre FAI pour se connecter. On accepte ensuite que la connexion soit automatiquement établie au démarrage. Drakconf va maintenant installer quelques packages. Ensuite nous redemandons le réseau quand on nous le demandera.

Vous pourrez voir a ce moment les lignes suivantes:

    :::text
    activation eth0
    activation eth1
    activation de la connexion inter

Si les trois tentatives se terminent par un échec, c'est simplement que vous avez connecté le modem et le réseau sur les mauvaises cartes ! Échangez donc le branchement des prises RJ-45, et redémarrez le PC. Pour redémarrer on peut faire un `ctrl+alt+suppr`. On aurait pu faire ça plus rapidement et proprement mais je veux vous faire voir qu'internet et le réseau se mettent en route automatiquement lors du démarrage, et ceci sans notre intervention.

Et si tout se passe bien, lors du reboot, on a:

    :::text
    activation eth0 -- OK
    checking internet connexion to start at boot -- OK

On peut ensuite vérifier qu'internet fonctionne en faisant un:

    :::bash
    $ ping google.com

Si finalement la connexion ne fonctionne pas, vérifier dans le fichier `/etc/sysconfig/network` que la variable `GATEWAYDEV` est positionnée sur l'interface ethernet qui est branchée au modem (`eth1` dans mon cas).

Pour récupérer une connexion rapide sous Mandrake 10, il suffit d'ajouter la ligne `alias net-pf-10 off` au fichier `/etc/modprobe.conf`, puis rebooter. Cela désactive le module `ipv6` qui est chargé par défaut.

Nous allons maintenant partager la connexion internet avec le réseau interne. Pour cela, nous allons installer un serveur `dhcp` sur notre passerelle pour distribuer automatiquement des adresses IP lorsqu'une machine va être connecté à notre réseau local.

Commençons par faire un:

    :::bash
    $ urpmi dhcp-server

Le serveur sera automatiquement lancé au démarrage de la machine, mais il faut le configurer.

Nous allons faire une copie d'un exemple de fichier de configuration, puis nous l'éditions:

    :::bash
    $ cp /etc/dhcpd.conf.sample /etc/dhcp.conf
    $ vi /etc/dhcpd.conf

Modifiez ce dernier pour qu'il contienne quelquechose comme:

    :::text
    ddns-update-style none;
    subnet 192.168.1.0 netmask 255.255.255.0 {
        range dynamic-bootp 192.168.1.128 192.168.1.254;
        default-lease-time 21600;
        max-lease-time 43200;
    }

Pour configurer les PC du réseau c'est très facile. Essayons par exemple de connecter ce laptop dur notre réseau. Ce laptop est également sous Mandrake 10, nous utilisons donc le panneau de configuration `drakconf`. Supprimons toutes les connexions si nécessaires, et ajoutons une nouvelle. Choisissez une connexion à travers un réseau local LAN, puis choisissons notre carte `eth0`. Dans l’écran suivant on choisis une attribution automatique de l'adresse IP via DHCP. Dans l’écran suivant on choisi un branchement à chaud du réseau et le lancement au démarrage. On donne ensuite un nom à la machine (par exemple `kevlaptop`). Maintenant on peut redémarrer le réseau avec `/etc/init.d/network restart` et constater avec un `ifconfig` que `eth0` se voit bien attribuer une IP de la forme `192.168.1.x` avec `x` comprit entre 128 et 254. On peut même pinguer la passerelle avec la commande `ping 192.168.1.1`.

Maintenant que n'importe lequel de nos pc est capable de se connecter au réseau et de communiquer avec n'importe lequel des autres pc, nous allons installer un serveur SSH et un serveur Webmin sur la passerelle pour obtenir un shell. Ce qui nous permettra de se passer de la carte graphique, de l'écran et du clavier de la passerelle. L’intérêt de supprimer tous ce matériel est de réduire la machine à son strict minimum pour gagner de la place et de l’énergie.

On installe donc le serveur SSH:

    :::bash
    $ urpmi openssh-server

Encore une fois, le serveur SSH sera lancé automatiquement lors du démarrage de la machine. Nous allons le vérifier en redémarrant la machine et en étant attentif au message:

    :::text
    lancement de sshd [OK]

Au lieu de configurer à la main le serveur SSH, nous allons utiliser Webmin, qui est une interface de configuration et d'administration web à distance. On fait donc un `urpmi webmin` pour l'installer. De la même manière ce deamon va ce lancer au démarrage. On redémarrera la machine pour être sur qu'il démarre comme nous le souhaitons.

Encore une fois, le message `lancement de webmin [OK]` nous en apporte la preuve !

Maintenant, pour utiliser Webmin, munissez vous de n'importe quel navigateur web depuis un PC sur votre réseau local et fait le pointer sur `https://192.168.1.1:1000`. Connectez vous avec le login `root` et le mot de passe qui va avec.

Dans l'onglet "servers" se trouve l'outil de configuration de DHCP. En cliquant dessus on retrouve la configuration que nous avons faite à la main.

Maintenant, retournons dans l'onglet "servers" et sélectionnons "ssh server". Nous allons configurer le serveur pour qu'il autorise la connexion de l'utilisateur `root`. Pour cela on se dirige dans la rubrique authentification et à la question "allow login by root" nous répondons "yes". Nous sauvegardons les modifications. Pour tester, nous utilisons une console sur le laptop pour se connecter sur la passerelle via un `ssh root@192.168.1.1`.

Si cela ne fonctionne pas c'est normal: la configuration de SSH à été enregistrée mais pas prise en compte. Il faut redémarrer le service.

Maintenant que nous pouvons prendre en main la passerelle avec SSH et Webmin, nous n'avons plus besoins du clavier, ni de la souris, de la carte graphique ou encore de l’écran. Nous allons donc arrêter la machine avec Webmin via l'onglet "system" et le module "bootup and shutdown". Tout en bas se trouve un bouton "shutdown system".

Allons faire un tour dans le bios, pour optimiser le démarrage de la machine. Dans les options de boot, on ne boutera que sur le disque dur principal, on ne demandera pas la vérification de la disquette (option "boot up floppy seek"), et on réglera tous les paramètres pour un démarrage le plus rapide possible. On fera aussi attention que le bios ne s’arrête pas si la clavier est absent.

Allumez votre PC et chronométrez le temps qui est nécessaire pour qu'il puisse démarrer. Une fois que vous avez cette valeur, arrêter le PC, enlever carte graphiques, clavier et souris. Allumez le PC en lançant le chronomètre. Une fois que le chrono est atteint, on va faire des tests pour être certain que la passerelle est opérationnelle. Pour moi il me faut 2 minutes et 30 secondes.

Après ce délai, je fait un `ping 192.168.1.1` pour vérifier que la passerelle est bien sur le réseau et répond. Ensuite je tente un `ssh root@192.168.1.1` et effectivement j'ai bien un shell sur la passerelle.

Maintenant je peut configurer entièrement ma passerelle via un PC extérieur.

Dans Webmin, on va dans `server` > `DHCP` > `edit client options`, pour mettre à jour la configuration du serveur DHCP et communiquer les coordonnées de notre passerelle. Voici les nouveaux paramètres:

  * Subnet mask: `255.255.255.0`
  * Default router: `192.168.1.1` (= l'IP de notre routeur)
  * DNS serveur: choisir un des deux DNS fournis par votre FAI

Ne pas oublier de forcer l'interface `eth0` comme interface de recherche DHCP par défaut, sinon le deamon aura du mal à démarrer au boot une fois sur deux.

Au final, on a un fichier `/etc/dhcpd.conf` qui doit ressembler à ça:

    :::text
    option subnet-mask 255.255.255.0;
    max-lease-time 43200;
    default-lease-time 21600;
    option domain-name-servers 212.151.136.242 , 212.151.136.246 , 130.244.127.161 , 130.244.127.162 , 130.244.127.169 , 130.244.127.170;
    option routers 192.168.1.1;
    ddns-update-style none;
    subnet 192.168.1.0 netmask 255.255.255.0 {
        option broadcast-address 192.168.1.255;
        range 192.168.1.128 192.168.1.254;
    }
    authoritative;

Nous allons installer `iptables` et le configurer:

    :::bash
    $ urpmi iptables
    $ echo 1 > /proc/sys/net/ipv4/ip_forward
    $ iptables -t nat -A POSTROUTING -o ppp+ -j MASQUERADE
    $ /etc/init.d/iptables save

Puis on édite `/etc/ssyconfig/network` pour y ajouter le paramètre suivant de façon à ce que l'IP forwaring soit activé au démarrage de la machine:

    :::text
    FORWARD_IPV4=yes

Nous allons configurer Urpmi pour qu'il puisse aller cherche tout seul les programmes à installer et les mises à jour sur internet. On peut utiliser [Easy Urpmi](http://easyurpmi.zarb.org) pour connaître les emplacement des repository de Mandrake.

On supprime d'abord la référence au CD-ROM:

    :::bash
    $ urpmi.removemedia -a

Ensuite on ajoute les sources `main`, `contrib`, `updates` et `plf`:

    :::bash
    $ urpmi.addmedia plf-free ftp://ftp.free.fr/pub/Distributions_Linux/plf/mandrake/free/10.1 with hdlist.cz
    $ urpmi.addmedia plf-nonfree ftp://ftp.free.fr/pub/Distributions_Linux/plf/mandrake/non-free/10.1 with hdlist.cz
    $ urpmi.addmedia --update updates ftp://ftp.proxad.net/pub/Distributions_Linux/Mandrakelinux/official/updates/10.1/main_updates with media_info/hdlist.cz
    $ urpmi.addmedia main ftp://ftp.proxad.net/pub/Distributions_Linux/Mandrakelinux/official/10.1/i586/media/main with media_info/hdlist.cz
    $ urpmi.addmedia contrib ftp://ftp.proxad.net/pub/Distributions_Linux/Mandrakelinux/official/10.1/i586/media/contrib with media_info/hdlist.cz

Pour tester que l'installation depuis le net fonctionne parfaitement, on peut installer `vim-enhanced`:

    :::bash
    $ urpmi vim-enhanced

Maintenant que nous pouvons chercher nos programmes depuis internet, le lecteur CD-ROM n'est plus utile. On arrête donc la machine avec la commande `shutdown -h now`, et on débranche physiquement le lecteur CD pour le ranger sur nos étagères. Lors du démarrage, le service `hardrake` va détecter l’absence du lecteur. Il va vous afficher une fenêtre de dialogue, que l'on va ignorer.

Nous allons programmer une mises a jour de sécurité tous les soirs vers 2 heure du matin. Cette action est possible grâce à la commande:

    :::bash
    $ /usr/sbin/urpmi.update -a && /usr/sbin/urpmi --update --auto --auto-select

Dans Webmin, cela se passe dans `system` > `scheduled cron jobs`. Cliquer sur `create a new cron job` pour ajouter la commande ci-dessus.

Testons la connexion ADSL.

En débranchant la prise RJ11 du modem, vérifier que le modem se reconnecte automatiquement. Sinon, vérifier que l'option `persist` est présente dans le fichier `/etc/ppp/peers/adsl`.

Dans mon cas j'ai une IP dynamique et mon FAI me déconnecte automatiquement toutes les 24h. J'ai remarqué que mon système supportait mal ce changement. Pour l'aider à se reconnecter j'ai créé un script en Python: [adsl-monitoring.py](https://github.com/kdeldycke/scripts/blob/master/adsl-monitoring.py).
