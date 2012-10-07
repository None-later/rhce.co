Date: 2012-10-06
Title: Create and configure LUKS-encrypted partitions and logical volumes to prompt for password and mount a decrypted file system at boot
Objective: 22
Category: c. Configure Local Storage - (RHCSA)
Tags: RHCSA


This is a brand new objective that was not present on the RHEL5 requirements. There are a few steps to this, but once you go through it a few times its not too bad. 

First step is to create a partition with fdisk or parted. We will use fdisk here.

    :::bash
    ~] fdisk -c -u /dev/sdb 

    Command (m for help): n
    Command action
    e   extended
    p   primary partition (1-4)
    p
    Partition number (1-4, default 1): 1
    First sector (2048-8388607, default 2048): 
    Using default value 2048
    Last sector, +sectors or +size{K,M,G} (2048-8388607, default 8388607): +200M 

    Command (m for help): t
    Selected partition 1
    Hex code (type L to list codes): 83 

    Command (m for help): w
    The partition table has been altered! 

    Calling ioctl() to re-read partition table.
    Syncing disks.

Now that the partition is created, we have to luks encrypt it. First we fill it with random data for security:

    :::bash
     ~] dd if=/dev/urandom of=/dev/sdb1 bs=1M
    dd: writing `/dev/sdb1': No space left on device
    201+0 records in
    200+0 records out
    209715200 bytes (210 MB) copied, 26.0497 s, 8.1 MB/s

Then we can encrypt the partition with luksFormat: 

    :::bash
     ~] cryptsetup luksFormat /dev/sdb1

    WARNING!
    ========
    This will overwrite data on /dev/sdb1 irrevocably. 

    Are you sure? (Type uppercase yes): YES
    Enter LUKS passphrase: 
    Verify passphrase: 

Now that the partition is encrypted, we open it and give it a label. The label is the name that it will show up as under /dev/mapper/  
 
    :::bash
    ~] cryptsetup luksOpen /dev/sdb1 mynew_data 
    Enter passphrase for /dev/sdb1:

Once the partition is setup and luks encrypted, it will be available in the /dev/mapper/ directory. You can do an ls on the /dev/mapper/ directory to confirm. 

    :::bash
    ~] ls /dev/mapper/
    control  mynew_data  VolGroup-lv_root  VolGroup-lv_swap

Next steps involve creating a filesystem, adding the partition into the /etc/crypttab file, as well as in the /etc/fstab file in order to configure automounting on boot. 

    :::bash
    ~] mkfs.ext4 /dev/mapper/mynew_data 
    mke2fs 1.41.14 (22-Dec-2010)
    Filesystem label=
    OS type: Linux
    Block size=1024 (log=0)
    Fragment size=1024 (log=0)
    Stride=0 blocks, Stripe width=0 blocks
    50800 inodes, 202752 blocks
    10137 blocks (5.00%) reserved for the super user
    First data block=1
    Maximum filesystem blocks=67371008
    25 block groups
    8192 blocks per group, 8192 fragments per group
    2032 inodes per group
    Superblock backups stored on blocks: 
    8193, 24577, 40961, 57345, 73729
    Writing inode tables: done                            
    Creating journal (4096 blocks): done
    Writing superblocks and filesystem accounting information: done

    This filesystem will be automatically checked every 25 mounts or
    180 days, whichever comes first.  Use tune2fs -c or -i to override
    ~] vim /etc/crypttab

In the /etc/crypttab file you would simply place the name of the encrypted device, as well as the path to the device:

 mynew_data      /dev/sdb1

Then we make the directory and add an entry into fstab, so that it mounts on boot:

    :::bash
    ~] mkdir /mynew_data
    ~] vim /etc/fstab
    
    # Add the following:
    /dev/mapper/mynew_data /mynew_data ext4    defaults    1 2


Thats it. You should run the mount command in order to verify your entries are correct in fstab, to prevent any boot issues.

    :::bash
    ~] mount -a
   
    ~] mount
    # .... lots of data here that im leaving out
    /dev/mapper/mynew_data on /mynew_data type ext4 (rw,relatime,seclabel,barrier=1,data=ordered)

Awesome, try that a few times and you should be good to go on setting up luks encrypted partitions.
