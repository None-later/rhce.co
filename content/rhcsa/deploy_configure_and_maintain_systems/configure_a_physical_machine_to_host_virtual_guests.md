Date: 2012-10-06
Title: Configure a physical machine to host virtual guests
Objective: 37
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

A default RHEL 6 system should come prepared to host virtual guests, minus the packages. In RHEL5 you had to make sure that you were running the xen kernel, which would require installing and booting into that kernel. RHEL 6 is simple, if it Virtualization is not installed, install it. 

    :::bash
    ~] yum groupinstall "Virtualization"

That will install everything needed to run virtual guests on RHEL 6. Easy huh?