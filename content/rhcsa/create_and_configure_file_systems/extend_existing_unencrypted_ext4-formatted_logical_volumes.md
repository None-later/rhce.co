Date: 2012-10-06
Title: Extend existing unencrypted ext4-formatted logical volumes
Objective: 29
Category: d. Create and Configure File Systems - (RHCSA)
Tags: RHCSA

Extending a file system without damaging it is an important skill, for many obvious reasons. Its also pretty straightforward once you know the commands. 

To extend a logical volume you can use the lvextend command, with the -L switch to specify the size. There are two ways to do this, make sure you are careful with the syntax. 

First lets display our logical volumes. (make sure you unmount any filesystems which you are about to extend.)

    :::bash
    ~] lvdisplay 
    --- Logical volume ---
    LV Name                /dev/MyNewVolgroup1/MyNewLogVol1
    VG Name                MyNewVolgroup1
    LV UUID                ZyZZLu-oQYu-ifti-ww28-VzQ7-xV5w-wOvBim
    LV Write Access        read/write
    LV Status              available
    # open                 0
    LV Size                200.00 MiB
    Current LE             50
    Segments               1
    Allocation             inherit
    Read ahead sectors     auto
    - currently set to     256
    Block device           253:2
   
Next we will extend the logical volume, adding 100M. See how we do this by putting a + sign in front of the size? 

    :::bash
    ~] lvextend -L +100M /dev/MyNewVolgroup1/MyNewLogVol1
    Extending logical volume MyNewLogVol1 to 300.00 MiB
    Logical volume MyNewLogVol1 successfully resized

Now we extend the volume TO BE 400M. So here we are specifying the end size, as opposed to adding that amount. This is an important distinction to make, especially during testing. Last thing you want to do is destroy a filesystem because you had to shrink it in order to meet the test requirements. 

    :::bash
    ~] lvextend -L 400M /dev/MyNewVolgroup1/MyNewLogVol1
    Extending logical volume MyNewLogVol1 to 400.00 MiB
    Logical volume MyNewLogVol1 successfully resized
