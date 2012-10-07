Date: 2012-10-06
Title: Diagnose and address routine SELinux policy violations
Objective: 55
Category: g. Manage Security - (RHCSA)
Tags: RHCSA

Going back to a previous example of trying to serve files from a directory other than the default apache directory, how would I be able to tell SELinux was the problem in that case?

I see a 403 error when I visit the domain after enabling SELinux. So first I would look in the apache error logs for a message as to why I am being denied. 

    [crit] [client 127.0.0.1] (13)Permission denied: /www/test/public_html/.htaccess pcfg_openfile: unable to check htaccess file, ensure it is readable

At this point it would be best to check permissions on the .htaccess file, and sure enough permissions are good. Apache user and Apache group owns it, and it is readable.

Next place to look would be the audit.log, which is the logfile that SELinux uses to log messages. 

    type=AVC msg=audit(1323618414.869:508): avc:  denied  { read } for  pid=23407 comm="httpd" name=".htaccess" dev=dm-2 ino=1966097 scontext=system_u:system_r:httpd_t:s0 tcontext=unconfined_u:object_r:user_home_t:s0 tclass=file
    type=SYSCALL msg=audit(1323618414.869:508): arch=c000003e syscall=2 success=no exit=-13 a0=7fa80ef2f358 a1=80000 a2=1b6 a3=7469672f7777772f items=0 ppid=1345 pid=23407 auid=4294967295 uid=48 gid=48 euid=48 suid=48 fsuid=48 egid=48 sgid=48 fsgid=48 tty=(none) ses=4294967295 comm="httpd" exe="/usr/sbin/httpd" subj=system_u:system_r:httpd_t:s0 key=(null)

I can see that /usr/sbin/httpd was denied access to '.htaccess'. At this point we know SELinux is the problem. Looking at the message a little closer, the context can be seen in the log entry, tcontext=unconfined_u:object_r:user_home_t, which is not the httpd_sys_content_t that can be seen on files in the deafult apache directory. 

Lets look at the ftpd man page, which has the best example to pull from...

    :::bash
    ~] man ftpd_selinux
 
    ...
    semanage fcontext -a -t public_content_t "/var/ftp(/.*)?"
    restorecon -F -R -v /var/ftp
    ...

Now replace the proper items in order to make this work:

    public_content_t >> httpd_sys_content_t
    "/var/ftp(/.*)?" >> "/www/test/public_html(/.*)?"
    /var/ftp >> /www/test/public_html

The commands we would end up running would be:

    :::bash
    semanage fcontext -a -t httpd_sys_content_t "/www/test/public_html(/.*)?"

And
    
    :::bash
    restorecon -F -R -v /www/test/public_html

Finally, check the context of that .htaccess file.

    :::bash
    ~] ls -laZ /www/test/public_html
     ...
     -rw-rw-r--. apache apache system_u:object_r:httpd_sys_content_t:s0 .htaccess
     ...

Looks good, now our page loads. This may seem kind of crazy, but practice with different application and after a while it will be second nature to troubleshoot this. This is a testable item now though, so you have to learn it.
