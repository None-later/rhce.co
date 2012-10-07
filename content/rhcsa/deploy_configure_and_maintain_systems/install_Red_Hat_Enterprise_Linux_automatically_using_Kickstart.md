Date: 2012-10-06
Title: Install Red Hat Enterprise Linux automatically using Kickstart
Objective: 36
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

Installing a system via Kickstart comes in pretty useful in real life. Whether there is time to do that in the 2.5 hours that they give you on the exam is questionable, but regardless its an objective.

There are a few ways to create a kickstart file, that would be used in the automatic installation of a Redhat Enterprise Linux 6 system. Theres always writing the thing from scratch, which while always an optoin, is not so efficient. Besides that there is:

- system-config-kickstart  (requires installing this application)

- using the anaconda-ks.cfg that was created during an installation. 

On the exam you would probably (hopefully) be provided with a premade kickstart file, so we work from there. 

Lets say we have this info:

    kickstart file = http://192.168.111.23/pub/ks/redhat6.kfg
    ip of new install = 192.168.111.222 (same subnet)
    netmask = 255.255.255.0

First we would boot the system with some sort of boot media, most likely the RHEL 6 CD-ROM #1 and at the boot prompt (when it asks you what you want to do) you would type a command like this, substituting your own info:

    linux ks=http://192.168.111.23/pub/ks/redhat6.kfg append ip=192.168.111.222 netmask=255.255.255.0

As long as everying is configured correctly and the installation media is where is should be, then this should install pretty hands off. Of course, anything besides this already configured environment would just take way too much time to be included on the exam. As long as you know how to install via ks file, you are probably good.