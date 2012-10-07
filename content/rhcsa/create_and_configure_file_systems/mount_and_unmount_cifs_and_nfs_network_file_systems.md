Date: 2012-10-06
Title: Mount and unmount CIFS and NFS network file systems
Objective: 27
Category: d. Create and Configure File Systems - (RHCSA)
Tags: RHCSA


Mounting network shares of type NFS and CIFS on Red Hat Enterprise Linux 6 is done with the mount command.

Mount CIFS share
==

Mounting samba/windows shares requires the -t cifs option followed by the //server:

    :::bash
    ~] mount -t cifs //server/share /mnt --verbose -o user=username

Unmount CIFS share
==

    :::bash
    ~] umount /mnt

Mount NFS share
==

Mounting a nfs share would be done with the -t nfs option, followed but the server:/mount 

    :::bash
    ~] mount -o rw -t nfs hostname:/mountpoint /mnt

Unmount NFS share
==

    :::bash
    ~] umount /mnt
