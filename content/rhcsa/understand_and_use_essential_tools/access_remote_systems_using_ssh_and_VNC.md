Date: 2012-10-04
Title: Access remote systems using ssh and VNC
Objective: 04
Category: 1. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA

SSH
===

Objective: Access remote systems using '''ssh''' and VNC

SSH is such an integrated part of this exam that its kind of weird that this is one of the official requirements. But nonetheless there are a number of different options that you can apply to make you more efficient in exam. 

Basic ssh access is simple:

    ::bash
    $ ssh user@host</code>

ssh to a custom port:

    ::bash
    $ ssh -p port_number user@host</code>

ssh bringing X (required to run programs like system-config-users remotely)

    ::bash
    $ ssh -X user@host</code>

ssh as another user (another way)

    ::bash
    $ ssh -l user host</code>

Display debugging messages as it connects. Useful if you have having some issues connecting to a certain machine.

    ::bash
    $ ssh -v user@host</code>

Those are the main options for ssh, as always "man ssh" to see all the other magic.

VNC
===

Objective: Access remote systems using ssh and '''VNC'''

On the remote machine, that you will be connecting to, you should have tigervnc-server installed.

    ::bash
    $ yum install tigervnc-server </code>

This puts a config file on your remote machine in /etc/sysconfig/vncservers

    ::bash
    VNCSERVERS="2:myusername"
    VNCSERVERARGS[2]="-geometry 800x600 -nolisten tcp -nohttpd"
 

Aside from changing "username" you want it to look like this. All we did to change it, is remove the "-localhost" directive. This would have restricted us from connecting from a remote system without a tunnel setup. Since this is an exam and not the real world, we can disable that.

Set up your password on the remote machine by running 

    ::bash
    $ vncpasswd</code>

And finally start your vncserver

    ::bash
    $ vncserver :1</code>

The output should look like this:<br>
    
    ::bash    
     [root@rhel6 ~]# vncserver :1
     New 'rhel6.local:1 (root)' desktop is rhel6.local:1<br>
     Starting applications specified in /root/.vnc/xstartup<br>
     Log file is /root/.vnc/rhel6.local:1.log
 
The default vnc client on Red Hat Enterprise Linux 6 is tigervnc. If it is not already installed on the system:

    ::bash
    $ yum install tigervnc</code>

To connect to the newly setup vncserver just type:

    ::bash
    $ vncviewer rhel6.local:5901 
(replace rhel6.local with your remote host)
