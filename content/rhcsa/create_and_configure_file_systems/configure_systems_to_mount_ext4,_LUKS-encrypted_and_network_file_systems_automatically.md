Date: 2012-10-06
Title: Configure systems to mount ext4, LUKS-encrypted and network file systems automatically
Objective: 28
Category: d. Create and Configure File Systems - (RHCSA)
Tags: RHCSA

Filesystems can be automatically mounted via path or UUID in the /etc/fstab file. 

Mount filesystems automatically
==

Via device:

    /dev/sda1   /mountpoint    ext4    defaults    1 1

Via filepath:

    /dev/mapper/filesystem /mountpoint ext4    defaults    1 1

Below are explainations of the fstab columns, right from the man page.

 * The first field (fs_spec)    - This field describes the block special device or remote filesystem to be mounted.
 * The second field (fs_file)   - This field describes the mount point for the filesystem.
 * The third field (fs_vfstype) - This  field  describes  the  type of the filesystem.
 * The fourth field (fs_mntops) - This field describes the mount options associated with the filesystem.
 * The fifth field (fs_freq)    - This  field is used for these filesystems by the dump(8) command to determine which filesystems need to be dumped. 
 * The sixth field (fs_passno)  - This field is used by the fsck(8) program to determine the order in which filesystem checks are done at reboot time. 

Mount ext4 filesystems
==

Assuming we have formatted /dev/sda1 as ext4, then we would add this line to fstab

    /dev/sda1   /mountpoint    ext4    defaults    1 1
 
Always check your entry by running mount -a command, if errors are returned address them before a reboot to prevent serious issues. 


Mount LUKS-encrypted filesystems
==

Assuming we have already created and opened a LUKS-encrypted filesystem, we would add the mount point and luks name into the /etc/crypttab file:

    lukspartition      /dev/mapper/lukspartition
 
and then we would want to mount add an entry to fstab. If we wanted to reference the filesystem via path:

    /dev/mapper/lukspartition   /mountpoint  ext4   defaults 0 0

If we wanted to reference by UUID we could get the UUID with the blkid command. 

    [root@localhost ~]# blkid
    /dev/mapper/newlukspart: UUID="51b401e1-2120-4f52-88ff-d6c80c379276" TYPE="ext4"
 
then in fstab:

    UUID="51b401e1-2120-4f52-88ff-d6c80c379276" /mountpoint     ext4   defaults 0 0
 
Mount network filesystems
==

Similar to the rest, just using ip as location, in `/etc/fstab`:

    192.168.1.100:/share    /mnt/share  nfs     ro,user,_netdev         0 0

The options will vary of course, 