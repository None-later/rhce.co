Date: 2012-10-04
Title: Use single-user mode to gain access to a system
Objective: 14
Category: b. Operate Running Systems - (RHCSA)
Tags: RHCSA


Booting into single user mode is the easiest way to gain access to a Red Hat Enterprise Linux server. 

This is only feasible if you have access to the physical console, which you will on the RHCSA and RHCE exams. 



 * At the beginning of the boot process you should see the grub menu pop up with a countdown and some kernel options (or perhaps just one option). 
 * It should be counting down at this point and says: "Press any key to enter the menu". In this case you would hit any key. 
 * At the bottom of the screen there is an explanation of the few options that are available to use on this page. One of these options is "e" for edit. Hit "e" to edit the boot kernel options. 
NOTE: (You can also use "a" for append, although they both accomplish the same thing.)
 * You would now edit the main kernel options, adding either "single" or even just "1" at the end. Once you have completed that hit enter, the "b" for boot. 
 * You are now in single user mode, and be auto logged in as root. 



 NOTE: for Red Hat Enterprise Linux 6.0 there is a bug that will prevent you from changing your root password in single user mode. This is a result of SELinux. For this situation you would want to temporarily disable SELinux.

    :::bash
    # setenforce 0

Now you should be allowed to change your root password.
