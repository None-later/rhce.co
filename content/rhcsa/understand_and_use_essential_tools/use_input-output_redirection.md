Date: 2012-10-04
Title: Use input-output redirection
Objective: 02
Category: 1. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA 

Input output redirection is one of the base skills you will need as a sysadmin. On the exam you will have to be able to redirect data from one command into another, and/or into a file. 

    :::bash
    $ echo "this is input" > file.txt

Another common example:

    :::bash
    $ cat /var/log/messages | less


Here are a couple of good tutorials already written on this:


[http://linuxhelp.blogspot.com/2006/01/inputoutput-redirection-made-simple-in.html](http://linuxhelp.blogspot.com/2006/01/inputoutput-redirection-made-simple-in.html)

[http://linuxcommand.org/lts0060.php](http://linuxcommand.org/lts0060.php)

[http://www.rwc.uc.edu/thomas/Intro_Unix_Text/IO_Redir_Pipes.html](http://www.rwc.uc.edu/thomas/Intro_Unix_Text/IO_Redir_Pipes.html)
