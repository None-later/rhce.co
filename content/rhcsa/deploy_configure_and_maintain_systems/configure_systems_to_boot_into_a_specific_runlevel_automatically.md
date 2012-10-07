Date: 2012-10-06
Title: Configure systems to boot into a specific runlevel automatically
Objective: 35
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

Depending on what the system running Red Hat Enterprise Linux 6 is going to be used for, you will want it to boot into the appropriate runlevel. 

This was already covered on this page: [http://rhce.co/rhel6/Boot_systems_into_different_runlevels_manually](http://rhce.co/rhel6/Boot_systems_into_different_runlevels_manually)

Configure system to boot into a runlevel automatically
==

The file that controls the runlevel that a system boots into is the /etc/inittab.

    # Default runlevel. The runlevels used are:
    #   0 - halt (Do NOT set initdefault to this)
    #   1 - Single user mode
    #   2 - Multiuser, without NFS (The same as 3, if you do not have networking)
    #   3 - Full multiuser mode
    #   4 - unused
    #   5 - X11
    #   6 - reboot (Do NOT set initdefault to this)
    # 
    id:5:initdefault:

In this case the default runlevel that this system will boot into is runlevel 5. Make note of what not to do. As noted above, do not set the default runlevel to 0 or 6, which is shutdown and reboot, for obvious reasons.
