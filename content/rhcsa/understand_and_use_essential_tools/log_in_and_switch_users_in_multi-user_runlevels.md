Date: 2012-10-04
Title: Log in and switch users in multi-user runlevels 
Objective: 05
Category: a. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA

If you have followed along to this point, you have logged in, and most likely been in either runlevel 3 or runlevel 5. Runlevels determine how much of the systems services are actually running. Most common runlevel for servers is going to be 3, most services that are not GUI oriented (including the Gnome Desktop) are turned off. Runlevel 5 is what you see when you boot into the desktop environment.

Switching between these levels is fairly straightforward. To switch to runlevel 3 type:

    :::bash
    $ init 3

Then to see what runlevel you are in type:

    :::bash
    $ runlevel

Switching between users, also straightforward. To switch to bob, assuming bob is a user on the system:

    :::bash
    $ su - bob  #note: We put the dash in there to gain the users login profile.
                # So if I switched to root and didnt use the - operator, I wouldn't have /usr/sbin in my path.

Switching to root is a common task.

    :::bash
    $ su - 