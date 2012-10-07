Date: 2012-10-06
Title: Configure systems to launch virtual machines at boot
Objective: 39
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

The virsh command is the command line utility, and the quickest way to accomplish this. But you always to have the option of messing around with the GUI, in case you forget this. 

To start a vm type:
--

    :::bash
    ~] virsh start machninename01

To shutdown:
--

    :::bash
    ~] virsh shutdown machninename01

To destroy 
--

This actually just means to bring the machine hard down, like pulling the plug on it. Not deleting it.

    :::bash
    ~] virsh destroy machninename01 

To gain access to a virtual console:
--

    :::bash
    ~] virsh console machninename01

To congifure the machine to launch at boot (autostart the virsh server):
--

    :::bash
    ~] virsh autostart machninename01