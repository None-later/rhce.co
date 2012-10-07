Date: 2012-10-06
Title: Schedule tasks using cron
Objective: 34
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

Cron is a utility used to schedule tasks to run at a certain time on various intervals. First is to make sure its installed, although it is installed by default on a normal installation. 

    ~] rpm -qa | grep cron
    cronie-1.4.4-2.el6.x86_64
    cronie-anacron-1.4.4-2.el6.x86_64

The easiest way to get guidance on how to use a utility is to use the man page. In this case the proper documentation is kind of hidden. 

    :::bash
    ~] man 5 crontab

This page lays out the options for cron, why its not found by simply using "man cron" is beyond me, but its not. 

The format for this goes as follows:

    *    *    *    *    *  command to be executed
    -    -    -    -    -
    |    |    |    |    |
    |    |    |    |    |
    |    |    |    |    +----- day of week (0 - 6) (Sunday=0)
    |    |    |    +---------- month (1 - 12)
    |    |    +--------------- day of month (1 - 31)
    |    +-------------------- hour (0 - 23)
    +------------------------- min (0 - 59)

An example of a cron job would be configuring a job to run every day on minute 0 hour 12 daily, or daily at 12:00pm. 

    0 12 * * * /bin/echo "some job" >> echo.log

Another example would be to run a job weekly at 3:30pm on Sunday

    30 15 * * 0 /bin/echo "another job" >> echo.log