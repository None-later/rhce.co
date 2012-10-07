Date: 2012-10-06
Title: Create, mount, unmount and use ext2, ext3 and ext4 file systems
Objective: 25
Category: d. Create and Configure File Systems - (RHCSA)
Tags: RHCSA

The default filesystem with Red Hat Enterprise Linux 6 is ext4, so that is the one we will use in the following example. The mkfs command can be used with the filesystem type as shown below. We are making a filesystem on a newly created partition, /dev/sdc1

Create file systems
==

    :::bash
    ~] mkfs.ext4 /dev/sdc1
    mke2fs 1.41.12 (17-May-2010)
    Filesystem label=
    OS type: Linux
    Block size=1024 (log=0)
    Fragment size=1024 (log=0)
    Stride=0 blocks, Stripe width=0 blocks
    64000 inodes, 256000 blocks
    12800 blocks (5.00%) reserved for the super user
    First data block=1
    Maximum filesystem blocks=67371008
    32 block groups
    8192 blocks per group, 8192 fragments per group
    2000 inodes per group
    Superblock backups stored on blocks: 
    8193, 24577, 40961, 57345, 73729, 204801, 221185

    Writing inode tables: done                            
    Creating journal (4096 blocks): done
    Writing superblocks and filesystem accounting information: done

    This filesystem will be automatically checked every 37 mounts or
    180 days, whichever comes first.  Use tune2fs -c or -i to override.

If we wanted to make an ext3 filesystem we would just run:

    :::bash
    ~] mkfs.ext3 /dev/sdc1

Mount Filesystems
==

To mount a newly created filesystem, we would use the mount command. First we have to create a mount point. 

    :::bash
    ~]  mkdir /new_mount_point

    ~]  mount -o rw -t ext4 /dev/sdc1 /new_mount_point/

To check that that partition was created and mounted correctly. 

    :::bash
    ~]  mount
    /dev/mapper/VolGroup-lv_root on / type ext4 (rw)
    ...output omitted
    /dev/sdc1 on /new_mount_point type ext4 (rw)

The mount will not survive a reboot, unless you add the partition into /etc/fstab as we did on this page: http://rhce.co/configure-systems-to-mount-file-systems-at-boot-by-universally-unique-id-uuid-or-label.html


Unmount Filesystems
==

The command to unmount a filesystem is not unmount, but instead its umount. (no idea why they left out the n, but they did)

    :::bash
    ~]  umount /dev/sdc1 
    :::bash
    ~]  mount
    # ... no /dev/sdc1 here
