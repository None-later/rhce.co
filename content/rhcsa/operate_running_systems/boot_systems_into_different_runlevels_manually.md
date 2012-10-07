Date: 2012-10-06
Title: Boot systems into different runlevels manually
Objective: 13
Category: b. Operate Running Systems - (RHCSA)
Tags: RHCSA

Red Hat Enterprise Linux is similar to most other linux distributions in its core functionality. The ability to run the operating system in multiple run levels is an important skill to have. 

If you type into your terminal:

    :::bash
    $ runlevel

you should see a number as the output. 

    :::bash
    $ N 3

This is the runlevel my server was running at the time this was written. 

There are 6 runlevels:

 *  Runlevel 0 - Halt
 *  Runlevel 1 - Single User mode. Most services turned off, including networking. Used to perform maintenance on the server usually. Boots logged into roots account, no  password.
 *  Runlevel 2 - This is basic functions, multi-user mode, without any networking. 
 *  Runlevel 3 - This is what servers usually run in, as it provides all of the services of the normal server, without the graphical user interface.
 *  Runlevel 4 - Doesn't really get used. 
 *  Runlevel 5 - This provides the same functions of runlevel 3, along with services to allow for desktop functionality (graphical user interface). 
 *  Runlevel 6 - Reboot

The command to jump runlevels is actually really easy. Just type init followed by the runlevel you want to switch into. 

    :::bash
    $ init 1

The above command would turn off most services and drop you into single user mode.
