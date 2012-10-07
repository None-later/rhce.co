Date: 2012-10-06
Title: Add new partitions, logical volumes and swap to a system non-destructively
Objective: 24
Category: c. Configure Local Storage - (RHCSA)
Tags: RHCSA

During the RHCSA / RHCE you may be asked to create new partitions on an already running system. This requires that you do so as not to disturb the already existing file systems, otherwise you may be reformatting halfway through the exam. 

Add new partitions
==

Adding new partitions is fairly straightforward using tools like fdisk or parted. We will be using fdisk for this objective. 

First step is to open the device that we want to make the partition on. 

    :::bash
    ~] fdisk -cu /dev/sdb 
    Device contains neither a valid DOS partition table, nor Sun, SGI or OSF disklabel
    Building a new DOS disklabel with disk identifier 0x110ea9fa.
    Changes will remain in memory only, until you decide to write them.
    After that, of course, the previous content won't be recoverable.

    Warning: invalid flag 0x0000 of partition table 4 will be corrected by w(rite)

You generally want to print the current partition table on the device with the p command
 
    :::bash
    Command (m for help): p

    Disk /dev/sdb: 2147 MB, 2147483648 bytes
    255 heads, 63 sectors/track, 261 cylinders, total 4194304 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x110ea9fa 

    Device Boot      Start         End      Blocks   Id  System

If nothing shows up under the list of devices, then there are no partitions. To make the first partition we will use the n command, for new. Then follow the prompts to create the new partition. Here we are making a 50MB partition.
 
    :::bash
    Command (m for help): n
    Command action
    e   extended
    p   primary partition (1-4)
    p
    Partition number (1-4): 1
    First sector (2048-4194303, default 2048): 
    Using default value 2048
    Last sector, +sectors or +size{K,M,G} (2048-4194303, default 4194303): +50M
 
Once you've created the partition its a good idea to print the partition table. Once you are happy with the changes, write them to the disk with the w command. 

    :::bash
    Command (m for help): p

    Disk /dev/sdb: 2147 MB, 2147483648 bytes
    255 heads, 63 sectors/track, 261 cylinders, total 4194304 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x110ea9fa 

    Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1            2048      104447       51200   83  Linux

    Command (m for help): w
    The partition table has been altered! 

    Calling ioctl() to re-read partition table.
    Syncing disks.


Add new logical volumes
==

To add a new logical volume you first need to create a new partition and set it to type Linux LVM.

    :::bash
    ~] fdisk -cu /dev/sdb 

    Command (m for help): p

    Disk /dev/sdb: 2147 MB, 2147483648 bytes
    255 heads, 63 sectors/track, 261 cylinders, total 4194304 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x110ea9fa

    Device Boot      Start         End      Blocks   Id  System

    Command (m for help): n
    Command action
    e   extended
    p   primary partition (1-4)
    p
    Partition number (1-4): 1
    First sector (2048-4194303, default 2048): 
    Using default value 2048
    Last sector, +sectors or +size{K,M,G} (2048-4194303, default 4194303): +50M


    Command (m for help): t
    Selected partition 1
    Hex code (type L to list codes): L

    0  Empty           24  NEC DOS         81  Minix / old Lin bf  Solaris        
    1  FAT12           39  Plan 9          82  Linux swap / So c1  DRDOS/sec (FAT-
    2  XENIX root      3c  PartitionMagic  83  Linux           c4  DRDOS/sec (FAT-
    3  XENIX usr       40  Venix 80286     84  OS/2 hidden C:  c6  DRDOS/sec (FAT-
    4  FAT16 <32M      41  PPC PReP Boot   85  Linux extended  c7  Syrinx         
    5  Extended        42  SFS             86  NTFS volume set da  Non-FS data    
    6  FAT16           4d  QNX4.x          87  NTFS volume set db  CP/M / CTOS / .
    7  HPFS/NTFS       4e  QNX4.x 2nd part 88  Linux plaintext de  Dell Utility   
    8  AIX             4f  QNX4.x 3rd part 8e  Linux LVM       df  BootIt         
    9  AIX bootable    50  OnTrack DM      93  Amoeba          e1  DOS access     
    a  OS/2 Boot Manag 51  OnTrack DM6 Aux 94  Amoeba BBT      e3  DOS R/O        
    b  W95 FAT32       52  CP/M            9f  BSD/OS          e4  SpeedStor      
    c  W95 FAT32 (LBA) 53  OnTrack DM6 Aux a0  IBM Thinkpad hi eb  BeOS fs        
    e  W95 FAT16 (LBA) 54  OnTrackDM6      a5  FreeBSD         ee  GPT            
    f  W95 Ext'd (LBA) 55  EZ-Drive        a6  OpenBSD         ef  EFI (FAT-12/16/
    10  OPUS            56  Golden Bow      a7  NeXTSTEP        f0  Linux/PA-RISC b
    11  Hidden FAT12    5c  Priam Edisk     a8  Darwin UFS      f1  SpeedStor      
    12  Compaq diagnost 61  SpeedStor       a9  NetBSD          f4  SpeedStor      
    14  Hidden FAT16 <3 63  GNU HURD or Sys ab  Darwin boot     f2  DOS secondary  
    16  Hidden FAT16    64  Novell Netware  af  HFS / HFS+      fb  VMware VMFS    
    17  Hidden HPFS/NTF 65  Novell Netware  b7  BSDI fs         fc  VMware VMKCORE 
    18  AST SmartSleep  70  DiskSecure Mult b8  BSDI swap       fd  Linux raid auto
    1b  Hidden W95 FAT3 75  PC/IX           bb  Boot Wizard hid fe  LANstep        
    1c  Hidden W95 FAT3 80  Old Minix       be  Solaris boot    ff  BBT            
    1e  Hidden W95 FAT1
    Hex code (type L to list codes): 8e
    Changed system type of partition 1 to 8e (Linux LVM) 

    Command (m for help): p 

    Disk /dev/sdb: 2147 MB, 2147483648 bytes
    255 heads, 63 sectors/track, 261 cylinders, total 4194304 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x110ea9fa

    Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1            2048      104447       51200   8e  Linux LVM 

    Command (m for help): w
    The partition table has been altered!

    Calling ioctl() to re-read partition table.
    Syncing disks.
 
Once you create the partition as Linux LVM type you can now create a physical volume with that partition. Keep in mind we are using small partitions in order to get the concept across, in real life these would be entire disks being added as physical volumes. 

To create a physical volume we use pvcreate:

    :::bash
    ~] pvcreate /dev/sdb1 physicalvol1
    Physical volume "/dev/sdb1" successfully created

    ~] pvdisplay  

    "/dev/sdb1" is a new physical volume of "50.00 MiB"
    --- NEW Physical volume ---
    PV Name               /dev/sdb1
    VG Name               
    PV Size               50.00 MiB
    Allocatable           NO
    PE Size               0   
    Total PE              0
    Free PE               0
    Allocated PE          0
    PV UUID               ysMMtz-jYei-tNph-tvSU-3sSy-vemf-sjWxbO


Next we have to create the volume group and add the physical volume to it. We can do this with the vgcreate command. 
    
    :::bash
    ~] vgcreate MyNewVolGroup /dev/sdb1
    Volume group "MyNewVolGroup" successfully created

Now that we have a physical volume, and its part of a volume group, so we can make a logical volume. To create a logical volume named LogVol1 from the volume group MyNewVolGroup we would use the following command. 

    :::bash
    ~] lvcreate -L 28M -n LogVol1 MyNewVolGroup
    Logical volume "LogVol1" created
   
Now there is a lovical volume named "LogVol1" that is a part of MyNewVolGroup"


'''''Add new swap partition'''''

Adding a swap partition is like adding any other partition, just changing his type to Linux Swap.

    :::bash
    ~] fdisk -cu /dev/sdb 

    Command (m for help): p

    Disk /dev/sdb: 2147 MB, 2147483648 bytes
    128 heads, 57 sectors/track, 574 cylinders, total 4194304 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x110ea9fa 

    Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1            2048      104447       51200   8e  Linux LVM

    Command (m for help): n
    Command action
    e   extended
    p   primary partition (1-4)
    p
    Partition number (1-4): 2
    First sector (104448-4194303, default 104448): +50M
    Value out of range.
    First sector (104448-4194303, default 104448):     
    Using default value 104448
    Last sector, +sectors or +size{K,M,G} (104448-4194303, default 4194303): ^C
    :::bash
    ~] fdisk -cu /dev/sdb 

    Command (m for help): n
    Command action
    e   extended
    p   primary partition (1-4)
    p
    Partition number (1-4): 2
    First sector (104448-4194303, default 104448): 
    Using default value 104448
    Last sector, +sectors or +size{K,M,G} (104448-4194303, default 4194303): +50M 

    Command (m for help): t
    Partition number (1-4): 2
    Hex code (type L to list codes): 82
    Changed system type of partition 2 to 82 (Linux swap / Solaris)

    Command (m for help): p

    Disk /dev/sdb: 2147 MB, 2147483648 bytes
    128 heads, 57 sectors/track, 574 cylinders, total 4194304 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0x110ea9fa 

    Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1            2048      104447       51200   8e  Linux LVM
    /dev/sdb2          104448      206847       51200   82  Linux swap / Solaris

    Command (m for help): w
    The partition table has been altered!

    Calling ioctl() to re-read partition table.
    Syncing disks.

To activate a swap partion.  
     
    :::bash
    ~] swapon -v /dev/sdb2
    swapon on /dev/sdb2
    swapon: /dev/sdb2: found swap signature: version 1, page-size 4, same byte order
    swapon: /dev/sdb2: pagesize=4096, swapsize=52428800, devsize=52428800

Confirm that the swap was added. 

    :::bash
    ~] swapon -s
    Filename               Type        Size    Used    Priority
    /dev/dm-1                               partition  1015800 0   -1
    /dev/sdb2                               partition  51192   0   -2
