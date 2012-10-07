Date: 2012-10-05
Title: List, set and change standard ugo/rwx permissions
Objective: 10
Category: a. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA

Permissions rule on compooters. Controlling them, essential. Linux has a number of different tools to do this, we list the essentials for the exam here.

<b>ls</b>
--
 
    :::bash
    # this is one of the most common commands used when probing a filesystem.
    # ls lists the files in a directory, and the -l switch shows permissions, 
    # ownership, size, and date modified 
    [root@rhel6 ~]# ls -l
    total 28
    -rw-------. 1 root root  1403 Mar 21 15:40 anaconda-ks.cfg
    -rw-r--r--. 1 root root 15932 Mar 21 15:39 install.log
    -rw-r--r--. 1 root root  5337 Mar 21 15:37 install.log.syslog

<b>chmod</b>
--

Permissions are as follows:

* 1 execute
* 2 write
* 4 read

..or in letter format

* x execute
* w write
* r read

*note: the first bit is reserved for type, files are -, directories are d, links are l*

For example, to change all three above files to 777 or readable, writable, and executable by all:
 
    :::bash
    # chmod changes permission bits, either with numeric or letter permission options.
    [root@rhel6 ~]# chmod 777 ./*
    [root@rhel6 ~]# ls -l
    total 28
    -rwxrwxrwx. 1 root root  1403 Mar 21 15:40 anaconda-ks.cfg
    -rwxrwxrwx. 1 root root 15932 Mar 21 15:39 install.log
    -rwxrwxrwx. 1 root root  5337 Mar 21 15:37 install.log.syslog
    
A more reasonable permissions set would be to allow others to read files, but only allow the owner to read, write, and execute. 

    :::bash
    [root@rhel6 ~]# chmod 644 ./*
    [root@rhel6 ~]# ls -l
    total 28
    -rw-r--r--. 1 root root  1403 Mar 21 15:40 anaconda-ks.cfg
    -rw-r--r--. 1 root root 15932 Mar 21 15:39 install.log
    -rw-r--r--. 1 root root  5337 Mar 21 15:37 install.log.syslog


Directories usually have a similar permissions set. They allow owner to rwx, but everyone else to rx. 755 would be the numerical value. 

*If directories are not executable, you cannot change into them with cd. cd essentially executes itself on the directory when you use it.*

If we want to use the letter format as opposed to numbers. we combine the ugo/rwx to apply permissions. To give the group permissions to execute install.log we combine g+x:

    :::bash
    [root@rhel6 ~]# chmod g+x install.log
    [root@rhel6 ~]# ls -l
    total 28
    -rw-r--r--. 1 nobody nobody  1403 Mar 21 15:40 anaconda-ks.cfg
    -rw-r-xr--. 1 david  root   15932 Mar 21 15:39 install.log
    -rw-r--r--. 1 root   david   5337 Mar 21 15:37 install.log.syslog

<b>chown</b>
--

chown is used to change ownership of files and directories. 

Using the same group of files, we can change the owner from root to david on install.log.

    :::bash
    [root@rhel6 ~]# chown david.david install.log
    [root@rhel6 ~]# ls -l
    total 28
    -rw-r--r--. 1 root  root   1403 Mar 21 15:40 anaconda-ks.cfg
    -rw-r--r--. 1 david david 15932 Mar 21 15:39 install.log
    -rw-r--r--. 1 root  root   5337 Mar 21 15:37 install.log.syslog

We can also change just group on a file, to allow the group certain permissions. Here we change install.log.syslog to be owned by group david, but still owner is root.

    :::bash
    [root@rhel6 ~]# chown root.david install.log.syslog 
    [root@rhel6 ~]# ls -l
    total 28
    -rw-r--r--. 1 root  root   1403 Mar 21 15:40 anaconda-ks.cfg
    -rw-r--r--. 1 david david 15932 Mar 21 15:39 install.log
    -rw-r--r--. 1 root  david  5337 Mar 21 15:37 install.log.syslog

If we don't want anyone to see have access, we could change it to a user like nobody. In this case, everyone would be able to read it, but nobody could write and execute anaconda-ks.config.

    :::bash
    [root@rhel6 ~]# chown nobody.nobody anaconda-ks.cfg 
    [root@rhel6 ~]# ls -l
    total 28
    -rw-r--r--. 1 nobody nobody  1403 Mar 21 15:40 anaconda-ks.cfg
    -rw-r--r--. 1 david  david  15932 Mar 21 15:39 install.log
    -rw-r--r--. 1 root   david   5337 Mar 21 15:37 install.log.syslog

<b>chgrp</b>

chgrp does the same thing as chown does, except it only changes the group. Handy if you just want to apply group permissions to a group of files that have various owners. 

    :::bash 
    [root@rhel6 ~]# chgrp root install.log
    [root@rhel6 ~]# ls -l
    total 28
    -rw-r--r--. 1 nobody nobody  1403 Mar 21 15:40 anaconda-ks.cfg
    -rw-r--r--. 1 david  root   15932 Mar 21 15:39 install.log
    -rw-r--r--. 1 root   david   5337 Mar 21 15:37 install.log.syslog
