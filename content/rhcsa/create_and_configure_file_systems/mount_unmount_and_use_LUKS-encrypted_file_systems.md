Date: 2012-10-06
Title: Mount, unmount and use LUKS-encrypted file systems
Objective: 26
Category: d. Create and Configure File Systems - (RHCSA)
Tags: RHCSA

To create a luks encrypted partition you would use the cryptsetup luksFormat command.

    :::bash
    ~] cryptsetup luksFormat /dev/sdc1 

    WARNING!
    ========
    This will overwrite data on /dev/sdc1 irrevocably. 

    Are you sure? (Type uppercase yes): YES
    Enter LUKS passphrase: 
    Verify passphrase: 

Once the partition is encrypted with a password, it needs to be opened with the password in order to be used. 

    :::bash
    ~] cryptsetup luksOpen /dev/sdc1 newlukspart
    Enter passphrase for /dev/sdc1:

Create a ext4 filesystem on the partition.

    :::bash
    ~] mkfs.ext4 /dev/mapper/newlukspart 
    mke2fs 1.41.12 (17-May-2010)
    Filesystem label=
    OS type: Linux
    Block size=1024 (log=0)
    Fragment size=1024 (log=0)
    Stride=0 blocks, Stripe width=0 blocks
    63488 inodes, 253952 blocks
    12697 blocks (5.00%) reserved for the super user
    First data block=1
    Maximum filesystem blocks=67371008
    31 block groups
    8192 blocks per group, 8192 fragments per group
    2048 inodes per group
    Superblock backups stored on blocks: 
    8193, 24577, 40961, 57345, 73729, 204801, 221185

    Writing inode tables: done                            
    Creating journal (4096 blocks): done
    Writing superblocks and filesystem accounting information: done

    This filesystem will be automatically checked every 29 mounts or
    180 days, whichever comes first.  Use tune2fs -c or -i to override. 

Create the mount point and mount read/write on that mount point.

    :::bash
    ~] mkdir /lukspart

    ~] mount -o rw -t ext4 /dev/mapper/newlukspart /lukspart

Check that the partition is mounted. 
    
    :::bash
    ~] mount -l
    ... output omitted... 
    /dev/mapper/newlukspart on /lukspart type ext4 (rw)

Finally the command to unmount the partition would just be umount. 

    :::bash
    ~] umount /lukspart
