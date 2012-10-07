Date: 2012-10-06
Title: Update the kernel package appropriately to ensure a bootable system
Objective: 44
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

Updating the kernel package in Red Hat Enterprise Linux 6 is easy, and as long as you update it with YUM, most everything is handled for you. 

    :::bash
    ~] yum update kernel

This should update the kernel, and update the `/boot/grub/grub.conf` file as well, to add the new kernel as the default kernel at boot time. We can verify this by checking the grub.conf before and after. You will notice that there is one more entry after the upgrade, and that it makes it the default. This also allows us to boot into an older kernel should we need to, at boot time.