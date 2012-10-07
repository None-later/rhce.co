Date: 2012-10-06
Title: List and identify SELinux file and process context
Objective: 52
Category: g. Manage Security - (RHCSA)
Tags: RHCSA

Listing and identifying SELinux context is really simple. You pretty much just add -Z to your query to display SELinux specific info along with your normal file attributes.

    :::bash
    ~] ps -Z
    LABEL                             PID TTY          TIME CMD
    unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 15802 pts/21 00:00:00 bash
    unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 15908 pts/21 00:00:00 ps

    ~] ls -lZ
    -rw-r--r--. root root system_u:object_r:httpd_config_t:s0 httpd.conf
    -rw-r--r--. root root system_u:object_r:httpd_config_t:s0 magic

This will allow you to see what context is currently applied to the file, and troubleshoot from there if need be.
