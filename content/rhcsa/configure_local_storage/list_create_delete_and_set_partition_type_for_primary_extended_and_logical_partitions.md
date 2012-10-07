Date: 2012-10-06
Title: List, create, delete and set partition type for primary, extended, and logical partitions
Objective: 20
Category: 3. Configure Local Storage - (RHCSA)
Tags: RHCSA

The official tool is now parted, but you can still use fdisk to create partitions. I'm a fan of fdisk, so thats what I will be using here. 

<b>List partitions</b>
--

To list all partitions that are on your server, you would issue the fdisk command, with the list switch.

    :::bash
    $ fdisk -l

<b>Create new partitions</b>
--

In order to create new partitions you would first have to open the device in fdisk. I will be opening /dev/sdb and creating both a primary and extended partition. We use the n command to create a new partition. 

    :::bash
    $ sudo fdisk /dev/sdb
 
    Command (m for help): n
    Command action
    e   extended
    p   primary partition (1-4)
    p
    Partition number (1-4, default 1): 1
    First sector (2048-8388607, default 2048): 
    Using default value 2048
    Last sector, +sectors or +size{K,M,G} (2048-8388607, default 8388607): +250M

    Command (m for help): p 

    Disk /dev/sdb: 4294 MB, 4294967296 bytes
    255 heads, 63 sectors/track, 522 cylinders, total 8388608 sectors
    Units = sectors of 1 * 512 = 512 bytes
    Sector size (logical/physical): 512 bytes / 512 bytes
    I/O size (minimum/optimal): 512 bytes / 512 bytes
    Disk identifier: 0xd26a7e50 

    Device Boot      Start         End      Blocks   Id  System
    /dev/sdb1            2048      514047      256000   83  Linux

    Command (m for help): n
    Command action
    e   extended
    p   primary partition (1-4)
    e
    Partition number (1-4, default 2): 
    Using default value 2
    First sector (514048-8388607, default 514048): 
    Using default value 514048
    Last sector, +sectors or +size{K,M,G} (514048-8388607, default 8388607): +500M

    Command (m for help): w
    The partition table has been altered!

    Calling ioctl() to re-read partition table.
    Syncing disks.
    $ sudo partprobe
 
<b>Delete partitions</b>
--

Deleting partitions is even easier. You would just type d at the fdisk prompt, tell it which partition number you are deleting, and the write the changes with the w flag. 

    :::bash
    $ sudo fdisk /dev/sdb
 
     Command (m for help): p
     
     Disk /dev/sdb: 4294 MB, 4294967296 bytes
     255 heads, 63 sectors/track, 522 cylinders, total 8388608 sectors
     Units = sectors of 1 * 512 = 512 bytes
     Sector size (logical/physical): 512 bytes / 512 bytes
     I/O size (minimum/optimal): 512 bytes / 512 bytes
     Disk identifier: 0x08bafe2e
     
       Device Boot      Start         End      Blocks   Id  System
     /dev/sdb1            2048     1026047      512000   83  Linux
     /dev/sdb2         1026048     1538047      256000    5  Extended
     
     Command (m for help): d
     Partition number (1-5): 2
     
     Command (m for help): p
     
     Disk /dev/sdb: 4294 MB, 4294967296 bytes
     255 heads, 63 sectors/track, 522 cylinders, total 8388608 sectors
     Units = sectors of 1 * 512 = 512 bytes
     Sector size (logical/physical): 512 bytes / 512 bytes
     I/O size (minimum/optimal): 512 bytes / 512 bytes
     Disk identifier: 0x08bafe2e
     
       Device Boot      Start         End      Blocks   Id  System
     /dev/sdb1            2048     1026047      512000   83  Linux 
     
     Command (m for help): w
     The partition table has been altered!
      
     Calling ioctl() to re-read partition table.
     Syncing disks.
     $ sudo partprobe

<b>Set partition type</b>
--

In order to use the disk we have to set a partition type. In this case we just make it a general Linux format #83. If it were going to be part of a raid array, we would make it Linux raid auto, #fd.

    :::bash
    $ fdisk /dev/sdb 
 
    Command (m for help): t
    Selected partition 1
    Hex code (type L to list codes): L 

    0  Empty           24  NEC DOS         81  Minix / old Lin bf  Solaris        
    1  FAT12           27  Hidden NTFS Win 82  Linux swap / So c1  DRDOS/sec (FAT-
    2  XENIX root      39  Plan 9          83  Linux           c4  DRDOS/sec (FAT-
    3  XENIX usr       3c  PartitionMagic  84  OS/2 hidden C:  c6  DRDOS/sec (FAT-
    4  FAT16 <32M      40  Venix 80286     85  Linux extended  c7  Syrinx         
    5  Extended        41  PPC PReP Boot   86  NTFS volume set da  Non-FS data    
    6  FAT16           42  SFS             87  NTFS volume set db  CP/M / CTOS / .
    7  HPFS/NTFS/exFAT 4d  QNX4.x          88  Linux plaintext de  Dell Utility   
    8  AIX             4e  QNX4.x 2nd part 8e  Linux LVM       df  BootIt         
    9  AIX bootable    4f  QNX4.x 3rd part 93  Amoeba          e1  DOS access     
    a  OS/2 Boot Manag 50  OnTrack DM      94  Amoeba BBT      e3  DOS R/O        
    b  W95 FAT32       51  OnTrack DM6 Aux 9f  BSD/OS          e4  SpeedStor      
    c  W95 FAT32 (LBA) 52  CP/M            a0  IBM Thinkpad hi eb  BeOS fs        
    e  W95 FAT16 (LBA) 53  OnTrack DM6 Aux a5  FreeBSD         ee  GPT            
    f  W95 Ext'd (LBA) 54  OnTrackDM6      a6  OpenBSD         ef  EFI (FAT-12/16/
    10  OPUS            55  EZ-Drive        a7  NeXTSTEP        f0  Linux/PA-RISC b
    11  Hidden FAT12    56  Golden Bow      a8  Darwin UFS      f1  SpeedStor      
    12  Compaq diagnost 5c  Priam Edisk     a9  NetBSD          f4  SpeedStor      
    14  Hidden FAT16 <3 61  SpeedStor       ab  Darwin boot     f2  DOS secondary  
    16  Hidden FAT16    63  GNU HURD or Sys af  HFS / HFS+      fb  VMware VMFS    
    17  Hidden HPFS/NTF 64  Novell Netware  b7  BSDI fs         fc  VMware VMKCORE 
    18  AST SmartSleep  65  Novell Netware  b8  BSDI swap       fd  Linux raid auto
    1b  Hidden W95 FAT3 70  DiskSecure Mult bb  Boot Wizard hid fe  LANstep        
    1c  Hidden W95 FAT3 75  PC/IX           be  Solaris boot    ff  BBT            
    1e  Hidden W95 FAT1 80  Old Minix      
    Hex code (type L to list codes): 83

    Command (m for help): w
    The partition table has been altered! 

    Calling ioctl() to re-read partition table.
    Syncing disks.

Redhat actually encourages the use of parted nowadays, with works a little differently. To see information about that, see this link [http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/s1-disk-storage-parted.html](http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/s1-disk-storage-parted.html)
