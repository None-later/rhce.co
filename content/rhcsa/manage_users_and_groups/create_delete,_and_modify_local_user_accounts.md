Date: 2012-10-06
Title: Create, delete, and modify local user accounts
Objective: 46
Category: f. Manage Users and Groups - (RHCSA)
Tags: RHCSA

Two ways you can go about this, the command-line way, or the GUI way. Doesn't matter for the test, just whatever you are comfortable with. Keep in mind that as a sysadmin it will be much more handy to use the command-line. ;-) 


Graphical User Interface (GUI)
==

    :::bash
    ~]  yum -y install system-config-users

    ~]  system-config-users

That will pop up an interface to add, remove, and modify users. Remember that if you are doing this remotely, you need to carry your XSession over to the server. 

    :::bash
    ~]  ssh -X user@host

That's as far as I will go into the GUI, its all point and click. :)

Command-line interface (CLI)
==

*Add user bob:*
--

    :::bash
    ~]  useradd bob

*Add bob into the wheel group*
--

    :::bash
    ~]  useradd -G wheel bob

*Add bob with sh shell instead of bash*
--

    :::bash
    ~]  useradd -s /bin/sh bob

*Add bob with a UID of 504 and a GID of 505*
--

    :::bash
    ~]  useradd -u 504 -g 505 bob

*Modify bob to use the bash shell instead*
--

    :::bash
    ~]  usermod -s /bin/bash bob

*Modify bob to be in the sales group as well*
--

    :::bash
    ~]  usermod -a -G sales bob

*Set or change a password for bob*
--

    :::bash
    ~]  passwd bob

*Delete bob from the system*
--

    :::bash
    ~]  userdel bob

*Delete bob and force remove him even if he is logged in. Also removes his home dir and mail spool*
--

    :::bash
    ~]  userdel -f bob

There are many other options that you can use that I didn't go over, just check out the man page. I covered most of the common ones.
