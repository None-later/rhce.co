Date: 2012-10-06
Title: Configure network services to start automatically at boot
Objective: 40
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

You could setup every service perfectly, with all the correct settings, but if they do not start at boot, it will all have been in vain. Starting services at boot is critical in the exam, as well as in real life. Luckily this is made very simple with Red Hat Enterprise Linux 6, and prior versions. 

To control network services behaviour on boot, the tool to use is '''chkconfig'''

These are best run while root or using sudo. Here I assume you are root. Here we check to see the status of httpd (apache). 

    :::bash
    ~] chkconfig --list | grep httpd
    httpd              0:off   1:off   2:on    3:on    4:on    5:on    6:off

Here we see six colums, one for each runlevel. Most common runlevels are 2-5, which we can see are on. If we want to turn that off, we would run the following:

    :::bash
    ~] chkconfig httpd off
    ~] chkconfig --list | grep httpd
    httpd              0:off   1:off   2:off   3:off   4:off   5:off   6:off

Now we can see they are off. This means if I reboot my machine, httpd will not automatically start on boot. To turn this back on for the common runlevels, just run:

    :::bash
    ~] chkconfig httpd on
    ~] chkconfig --list | grep httpd
    httpd              0:off   1:off   2:on    3:on    4:on    5:on    6:off

You can also specify only certain runlevels such as runlevel 3. Which is used for most web servers. 

    :::bash
    ~] chkconfig --level 3 httpd on
    ~] chkconfig --list | grep http
    httpd              0:off   1:off   2:off   3:on    4:off   5:off   6:off

So make sure you double check the service that you are depending on, both on exam day and real life.
