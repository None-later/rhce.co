Date: 2012-10-06
Title: Start, stop and check the status of network services
Objective: 19
Category: 2. Operate Running Systems - (RHCSA)
Tags: RHCSA


There are a few things to consider when dealing with network services:

1. You want to make sure the service is running, if not start it. 

2. You want to be able to restart the service, to reload a config file that you may have changed.

3. You want to have the ability to turn the service off, if you don't plan on using it. 

4. Also, you need to be able to set the service up to start on boot, or vise versa.


Service management takes place with the service command. Go figure. 

To start the httpd service, you would type:

    :::bash
    $ sudo /sbin/service httpd start

To stop it:

    :::bash
    $ sudo /sbin/service httpd stop

To restart it:
    
    :::bash
    $ sudo /sbin/service httpd restart

To reload it (refresh configs without stopping and starting):

    :::bash 
    $ sudo /sbin/service httpd reload

How do you know what services you can do that with? Well that can be listed with the tool that will handing startup programs. chkconfig.

chkconfig is used to manage what runlevel a program with automatically start or get killed in. To list all your services you would just type

    :::bash
    $ sudo /sbin/chkconfig --list

Thats a big list. But you get the idea, you can see how they are either on or off in each runlevel. To narrow down the list we can use grep to process the list and filter out say, our httpd service.

    :::bash
    $ sudo /sbin/chkconfig --list | grep httpd
    httpd              0:off   1:off   2:on    3:on    4:on    5:on    6:off

So we can see that in runlevels 2-5 we have httpd on in. If that were not the case, and my server rebooted, when it came back up all my sites would be disabled, until I manually went in and started the service. 

To change the values of that you would just run chkconfig followed by the service and whether you want to on or off in the main runlevels. 

    :::bash    
    $ sudo /sbin/chkconfig httpd on

You can actually control what runlevels you want the service on in as well by adding the --level switch followed by the runlevels. 

    :::bash
    $ sudo /sbin/chkconfig --level 45 httpd off
    $ sudo /sbin/chkconfig --list | grep httpd
    httpd           0:off   1:off   2:on    3:on    4:off   5:off   6:off

I turned off the httpd service for runlevel 4 and 5 there.
