Date: 2012-10-06
Title: Restore default file contexts
Objective: 53
Category: g. Manage Security - (RHCSA)
Tags: RHCSA

Restore default file contexts
==

If any files are added to say, /www/testsite/, and you are running SELinux in enforcing mode, then you will likely have an issue when trying to serve them via Apache. This is because their SELinux file context is not that of `httpd_sys_content_t` in that custom directory. SELinux is strict in that nature, and requires that you apply the proper context before it will allow Apache to use them.

The easiest thing to do is reference the man pages for specific syntax. I'll use the example of restoring context to files added into a directory that will be used by apache, but isnt the default system directory. I copied an index.html file into /www/testsite

    :::bash
    ~] ls -laZ /www/testsite/
    -rw-r--r--. root      root      unconfined_u:object_r:default_t:s0 index.html

You can see this file has a generic file context. When running in "Enforcing", SELinux will throw permission errors if this page is served via apache. To set proper file contexts, semanage is the tool to use. 

*Tip: "man -k _selinux" will show you the man pages for the main applications you will be using, ftpd, httpd, etc. There are good examples in there*

First we set context of the directory...

    :::bash
    ~] semanage fcontext -a -t httpd_sys_content_t "/www/testsite(/.*)?"

Next we restore context recursively...

    :::bash
    ~] restorecon -F -R -v /www/testsite
    restorecon reset /www/testsite context unconfined_u:object_r:default_t:s0->system_u:object_r:httpd_sys_content_t:s0
    restorecon reset /www/testsite/index.html context unconfined_u:object_r:default_t:s0->system_u:object_r:httpd_sys_content_t:s0

Now Apache will have no problem serving files from that directory, because SELinux will be happy with the context. 

NOTE: If this didnt happen, and you got an error that semanage isnt found, then you didnt install the package that provides this tool.

    :::bash
    ~] yum install policycoreutils-python

Make sure you remember this, it could kill your ability to properly perform SELinux tasks on an exam!
