Date: 2012-10-06
Title: Set enforcing and permissive modes for SELinux
Objective: 51
Category: g. Manage Security - (RHCSA)
Tags: RHCSA

With SELinux being part of the exams now, this is important. Knowing how to change modes and detect mode in SELinux is key.

To check the current SELinux mode

    :::bash
    ~]  getenforce

To set the SELinux mode to 0 (does not persist through a reboot)

    :::bash
    ~]  setenforce 0

To change mode persistently

    :::bash
    ~]  vim /etc/selinux/config

change to desired value: disabled, permissive, enforcing

    SELINUX=disabled
    
{: .note }
>
> Keep in mind that, after editing */etc/selinux/config* changes will be applied after system reboot.