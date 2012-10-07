Date: 2012-10-06
Title: Create and manage Access Control Lists (ACLs)
Objective: 31
Category: d. Create and Configure File Systems - (RHCSA)
Tags: RHCSA

Access control lists are an import part of administration on any Red Hat Enterprise Linux 6 system that you will be managing. The ability to deny or allow users based on user or group is crucial. 

Enable ACL on a filesystem
==

To use ACLs first the acl property needs to be enabled on the partition. This can be checked by running the mount command and checking the options section for acl. 

    :::bash
    ~] mount
    /dev/mapper/vg_rhel01-lv_root on / type ext4 (rw)

Notice that the only option is "rw", which means that acl is not enabled on the root filesystem. The change is easy to make and it involves adding an option in /etc/fstab. 

    :::bash
    ~] vim /etc/fstab

before:

    /dev/mapper/vg_rhel01-lv_root /                       ext4    defaults        1 1

after:

    /dev/mapper/vg_rhel01-lv_root /                       ext4    defaults,acl        1 1

Once that change has been made, we need to remount the filesystem in order for it to actually take effect. We could reboot, or just run the mount command with an option of remount. 

    :::bash
    ~] mount -o remount /
    
    ~] mount
    /dev/mapper/vg_rhel01-lv_root on / type ext4 (rw,acl)

Now the acl option shows next to "rw". 

Apply ACLs to a file for a user
==

To check acl on a directory or file, we would use the getfacl command 

    :::bash
    ~] getfacl install.log
    # file: install.log
    # owner: root
    # group: root
    user::rw-
    group::r--
    mask::r--
    other::r--

There are no special rules applied at this point. Use the setfacl command to add rw permissions to install.log.

    :::bash
    ~] setfacl -m u:user2:rw install.log

Then getfacl to see the newly added acl. 

    :::bash
    ~] getfacl install.log
    # file: install.log
    # owner: root
    # group: root
    user::rw-
    user:user2:rw-
    group::r--
    mask::rw-
    other::r--

Apply ACLs to a file for a group
==

To add a group acl on the same file, we use the g option instead. The following command with add rwx permissions for the group "it" on the install.log file. 

    :::bash
    ~] setfacl -m g:it:rwx install.log
    ~] getfacl install.log
    # file: install.log
    # owner: root
    # group: root
    user::rw-
    user:user2:rw-
    group::r--
    group:it:rwx
    mask::rwx
    other::r--
