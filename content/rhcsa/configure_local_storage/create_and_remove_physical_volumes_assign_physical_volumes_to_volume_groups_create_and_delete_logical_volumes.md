Date: 2012-10-06
Title: Create and remove physical volumes, assign physical volumes to volume groups, create and delete logical volumes
Objective: 21
Category: c. Configure Local Storage - (RHCSA)
Tags: RHCSA

Create and remove physical volumes
===

Creating a physical volume in LVM is the first step in the LVM setup. Its the part where you actually tell Red Hat Enterprise Linux that you want a disk to be used for LVM.

*`pvcreate`* is the command used to add the physical volumes, or physical partitions.

    :::bash
    ~] pvcreate /dev/sdb
    ~] Physical volume "/dev/sdb" successfully created

*`pvremove`* is used to disassociate the volume from LVM.

    :::bash
    ~] pvremove /dev/sdb
    ~] Labels on physical volume "/dev/sdb" successfully wiped

Assign physical volumes to volume groups
===

Once that physical volume has been created we can add it to a volume group with the vgcreate or vgextend (if the volume group has already been created).

If the volume group does not exist, you can create it and add physical volumes in one shot:

    :::bash
    ~] vgextend MyVolGroup /dev/sdc 
    No physical volume label read from /dev/sdc
    Physical volume "/dev/sdc" successfully created
    Volume group "MyVolGroup" successfully extended


To assign a new physical volume to an existing volume group we use *`vgextend`*:

    :::bash
    ~] vgextend MyVolGroup /dev/sdc 
    Volume group "MyVolGroup" successfully extended

Similarly if we want to remove /dev/sdc from that group we would run ''vgreduce'':

    :::bash
    ~] vgreduce MyVolGroup /dev/sdc
    Removed "/dev/sdc" from volume group "MyVolGroup"

Create and delete logical volumes
==

Logical Volumes have similar commands to create and delete as Volume Groups and Physical Volumes. 

To create a new logical volume:

    :::bash
    ~] lvcreate -L 100M MyVolGroup
    Logical volume "lvol0" created

To display the volume after for confirmation:

    :::bash
    ~] lvdisplay MyVolGroup
    --- Logical volume ---
    LV Name                /dev/MyVolGroup/lvol0
    VG Name                MyVolGroup
    LV UUID                zwLMev-i63w-7Jpk-XuqZ-VGl7-89Ov-WpoewP
    LV Write Access        read/write
    LV Status              available
    # open                 0
    LV Size                100.00 MiB
    Current LE             25
    Segments               1
    Allocation             inherit
    Read ahead sectors     auto
    - currently set to     256
    Block device           253:2

To delete the logical volume you would use the LV Name listed in the results of lvdisplay:

   :::bash
    ~] lvremove /dev/MyVolGroup/lvol0
    Do you really want to remove active logical volume lvol0? [y/n]: y
    Logical volume "lvol0" successfully removed
