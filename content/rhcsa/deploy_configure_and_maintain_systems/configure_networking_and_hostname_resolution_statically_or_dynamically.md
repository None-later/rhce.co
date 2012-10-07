Date: 2012-10-06
Title: Configure networking and hostname resolution statically or dynamically
Objective: 33
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

Configure networking
==

Networking is a big part of the RHCSA and RHCE. If you aren't super comfortable with configuring networking via network config files, then its probably a good idea to use the network management tools available. 

In Red Hat Enterprise Linux you can type "setup" at the command line. This will open up the Text Mode Setup Utility, which allows you to configure network, firewall, athentication, keyboard, RHN, and System Services. 

If you do venture into the networking configuration files, these are the important ones:

- `/etc/hosts`                                 The static table lookup for hostnames
- `/etc/resolv.conf`                           The resolver configuration file
- `/etc/sysconfig/network`                     Contains hostname setting
- `/etc/sysconfig/network-scripts/ifcfg-eth0`  The first network device configuration

These are files that will be essential to know about during the exam if you are altering config files. 

There will no doubt be some need to configure networks during the RHCSA and RHCE, so either way be prepared to fix network connections. 

Configuring the hostname
==

Configuring the hostname can be done in the /etc/sysconfig/network file. Edit this file with the updated hostname and then on reboot, the new hostname will be reflected.

    :::bash
    ~] vim /etc/sysconfig/network
    NETWORKING=yes
    HOSTNAME=rhel-01
