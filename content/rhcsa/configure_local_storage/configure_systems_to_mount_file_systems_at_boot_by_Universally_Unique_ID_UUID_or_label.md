Date: 2012-10-06
Title: Configure systems to mount file systems at boot by Universally Unique ID (UUID) or label
Objective: 23
Category: c. Configure Local Storage - (RHCSA)
Tags: RHCSA

Configuring a filesystem to mount via UUID or label is an essential part of managing filesystems and partitions on the Red Hat Enterprise Linux system, and will most probably be something you will see on an RHCSA/RHCE exam. 

First we will configure mounting at boot time via UUID. *To find the UUID of a device you have to issue just one command:*

    :::bash
    ~] blkid
    /dev/sda1: UUID="183e5753-fbe7-4cf7-b974-f6cb9a326a33" TYPE="ext4" 
    /dev/sda2: UUID="1OJDNK-4gpP-s3YE-cK7o-1urJ-cXHk-jPnuF7" TYPE="LVM2_member" 
    /dev/sdb1: UUID="1c1fa5a2-11e5-4d6b-89e9-61a15dcbe0f6" TYPE="crypto_LUKS" 
    /dev/mapper/VolGroup-lv_swap: UUID="dc82e68f-f1b9-409d-a1f7-c556eb6eb78a" TYPE="swap" 
    /dev/sdc: UUID="vFLamh-rudP-T1jc-ZrrH-LTgD-FUuq-IHUBgM" TYPE="LVM2_member" 
    /dev/mapper/VolGroup-lv_root: UUID="5bbc084b-1af0-464f-8629-9490a75cacd9" TYPE="ext4" 
    /dev/mapper/mynew_data: UUID="f8b694a6-916d-4ffa-8e5c-a7ed8ab25b5d" TYPE="ext4"

Once you have the UUID you can head over to /etc/fstab to create the entry. Here we will pick our new luks partition.

    :::bash
    ~] vim /etc/fstab

Inside of fstab we need to add a line. (if you already have a line for this partition, comment it out with #)

 UUID=f8b694a6-916d-4ffa-8e5c-a7ed8ab25b5d  /mynew_data ext4    defaults    1 2

Then write/save the file and quit :wq
You can confirm that this is entered correctly by using the mount command:

    :::bash
    ~] mount -a

    ~] mount
    ..ommitted data...
    /dev/mapper/mynew_data on /mynew_data type ext4 (rw,relatime,seclabel,barrier=1,data=ordered)

*Now to mount a filesystem via label* requires another step, to label the filesystem. Luckily this is done in one easy step using e2label. I am going to label the filesystem luksdrive

    :::bash
    ~] e2label /dev/mapper/mynew_data luksdrive

Now we can unmount the filesystem, change our fstab to use a label, and run mount a again to see it mounted via label instead. 

    :::bash
    ~] umount /mynew_data/
 
Verify its unmounted
 
    :::bash
    ~] mount

Then edit /etc/fstab this time using LABEL=luksdrive in place of UUID. So the line should look like:
 
    :::bash
    LABEL=luksdrive         /mynew_data             ext4    defaults        1 2

Run mount -a and mount to confirm:

    :::bash
    ~] mount -a

    ~] mount
    ..ommitted data...
    /dev/mapper/mynew_data on /mynew_data type ext4 (rw,relatime,seclabel,barrier=1,data=ordered)

Thats all there is to that. I would try that out a number of times to make sure you have the process down. Repitition is key.
