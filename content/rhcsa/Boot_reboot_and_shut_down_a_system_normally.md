Date: 2012-10-06
Title: Boot, reboot, and shut down a system normally
Objective: 12
Category: 1. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA 

Basically, they are referring to these actions on the command line. I'm sure everyone is able to do this on a pc, but not necessarily a live Red Hat Enterprise Linux Server remotely. 

The commands are simple for the server. 


Normal reboot

    $ sudo reboot

Another way

      $ sudo shutdown -r now

Changing to init 6 will reboot as well, which is what init 6 does. 

      $ sudo init 6

On the same note, init 0 calls all of the shutdown scripts and gracefully shuts down your machine.

      $ sudo init 0

Surprisingly you can also use the shutdown command to shutdown completely by using the -h switch.

      $ sudo shutdown -h

I think we all know how to boot the computer, so that shouldn't be a problem. :-)