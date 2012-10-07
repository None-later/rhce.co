Date: 2012-10-06
Title: Configure a system to run a default configuration FTP server
Objective: 42
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

FTP
==

vsftpd installs with a default configuration that works for this requirement. So a basic:

    :::bash
    ~] yum install vsftpd

    ~] chkconfig vsftpd on

This will get your default server up and running. But what about firewall and selinux?

Iptables
==

For iptables you want to open up port 20 and 21, to allow ftp requests in. 

    :::bash
    ~] iptables -I INPUT 5 -p tcp -m tcp --dport 20 -j ACCEPT

    ~] iptables -I INPUT 5 -p tcp -m tcp --dport 21 -j ACCEPT

Then remember to always save your iptables rules so they survive a reboot. 

Selinux
==

SELinux is now a part of the exams, so you have to know how to apply the correct context to the directories that will be used by vsftpd.

Here's a tip: All this information is stored in man pages, so rather than memorizing, use the resources available. If you search for _selinux, then all services that have information on how to be configured with SELinux will show up. To search the man pages use:

    :::bash
    ~] man -k _selinux
    ftpd_selinux         (8)  - Security-Enhanced Linux policy for ftp daemons

    ~] man ftpd_selinux
 
To make a ftp server's content available you can see it says to run the following:

    semanage fcontext -a -t public_content_t "/var/ftp(/.*)?"
     
    restorecon -F -R -v /var/ftp


Thats it. As long as you can install the application, vsftpd, open the correct ports in iptables, and set context in SELinux, then you are good to go on this objective.