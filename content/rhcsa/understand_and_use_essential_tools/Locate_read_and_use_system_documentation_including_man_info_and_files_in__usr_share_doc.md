Date: 2012-10-05
Title: Locate, read and use system documentation including man, info, and files in /usr/share/doc
Objective: 11
Category: a. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA

Man pages, docs, and info are all saving graces on the exams. 

The most commonly used help pages are **man pages**. 

    :::bash
    $ man vim 
 

This will give you the manual pages, with descriptions of the options, examples, and information about the application. If you don't remember exactly what man page you need, but you know what utility you are trying to use you can search man pages. 

For example, lets find all man pages relating to LVM.

    :::bash
    [root@rhel6 ~]# man -k lvm
    README.vmesa [perlvmesa] (1)  - building and installing Perl for VM/ESA
    lvm                  (8)  - LVM2 tools
    lvm.conf [lvm]       (5)  - Configuration file for LVM2
    lvmchange            (8)  - change attributes of the logical volume manager
    lvmconf              (8)  - LVM configuration modifier
    lvmdiskscan          (8)  - scan for all devices visible to LVM2
    lvmdump              (8)  - create lvm2 information dumps for diagnostic purposes
    lvmsadc              (8)  - LVM system activity data collector
    lvmsar               (8)  - LVM system activity reporter
    perlvms              (1)  - VMS-specific documentation for Perl
    pvcreate             (8)  - initialize a disk or partition for use by LVM
    pvresize             (8)  - resize a disk or partition in use by LVM2

This is helpful output of results from the search. Really helpful in situations that you forgot the name of a certain utility.

Info is nearly identical, referencing the info docs. Its not quite as nice to use, and therefore is not as popular. 

You could also get information from the /usr/share/docs. Here you can find other information about the program itself, or that particular version. The following output is a typical doc directory.

    :::bash
    [root@rhel6 yum-3.2.27]# pwd
    /usr/share/doc/yum-3.2.27
    [root@rhel6 yum-3.2.27]# ls
    AUTHORS  ChangeLog  COPYING  INSTALL  README  TODO


As you can see its very different, simply text files with license, readme, install instructions, etc. For most of your referencing in an exam situation, use the man pages.

*Exam tip: If you dont get any output from man pages, try running the following command, which will build the man pages.*

    :::bash
    # first check for the package
    [root@rhel6 ~]# rpm -qi man
    # then if its installed try
    [root@rhel6 ~]# makewhatis &
