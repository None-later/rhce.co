Date: 2012-10-04
Title: Identify CPU/memory intensive processes, adjust process priority with renice, and kill processes
Objective: 15
Category: 2. Operate Running Systems - (RHCSA)
Tags: RHCSA

A few commands to help you identify processes on the exam are ps and top. These are commands that you will actually use extensively to monitor systems in the workplace. 


ps - report a snapshot of the current processes.

ps helps you see what processes are being run, what files and commands they are being run with, who they are being run by, as well and their process ids. All the above items are crucial when troubleshooting issues on a Red Hat Enterprise Linux 6 system. 

a few good examples pulled from a man page:

EXAMPLES


    :::bash
    # To see every process on the system using standard syntax:
    $ ps -e
    $ ps -ef
    $ ps -eF
    ps -ely

    # To see every process on the system using BSD syntax:
    $ ps ax
    $ ps axu

    # To print a process tree:
    $ ps -ejH
    $ ps axjf

    # To get info about threads:
    $ ps -eLf
    $ ps axms

    # To get security info:
    $ ps -eo euser,ruser,suser,fuser,f,comm,label
    $ ps axZ
    $ ps -eM

    # To see every process running as root (real & effective ID) in user format:
    $ ps -U root -u root u

There is plenty of more info on this in the man pages as well as a plethoura of information on the web for ps. 

    :::bash
    top - display Linux tasks

At its most basic usage you can just type:

 <code>$ top </code>

There is a whole lot of options that go along with that command: "man top" to see them all.

renice — alter priority of running processes

As stated in the description, renice is a linux utility to change the priority of a process. This could obviously come in handy while trying to keep a process at bay. 

Example from the man page:

     renice +1 987 -u daemon root -p 32

This would change the priority of process ID's 987 and 32, and all processes owned by users daemon and root.

Man Page http://linux.die.net/man/8/renice

kill - terminate a process

Like it states in the name, this kills processes. Once you have identified the process you would like to kill with top or ps, you would use the kill command to terminate that process. 

The most common implementation of this is:

 <code># kill 2342 </code>

If that doesnt kill the process you would use the -9 switch, which will take out most any process. 

 <code># kill -9 2342</code>

NOTE: The -9 command should be used with caution. Make sure you are killing the right pid, otherwise terrible things may transpire, especially on the RHCSA or the RHCE, where time is of concern.
