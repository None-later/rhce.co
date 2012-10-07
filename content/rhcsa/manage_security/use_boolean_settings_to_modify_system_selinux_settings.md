Date: 2012-10-06
Title: Use boolean settings to modify system SELinux settings
Objective: 54
Category: g. Manage Security - (RHCSA)
Tags: RHCSA

As stated in the man page "Policy booleans enable runtime customization of SELinux policy." Booleans consist of a number of config items, that can either be on or off.

Easiest way to see the booleans currently set:

    :::bash
    ~] getsebool -a
    # ... long list

If I wanted to see booleans associated with httpd, I could just grep through that.

    :::bash
    ~] getsebool -a | grep httpd
    allow_httpd_anon_write --> off
    allow_httpd_mod_auth_ntlm_winbind --> off
    httpd_enable_cgi --> on
    ....

To change a boolean setting, setsebool would be the command to use. 

    :::bash
    ~] setsebool -P httpd_enable_cgi off

Notice the -P we add in there, that is to make the change persistant across a reboot. -P causes the boolean to be written into the policy file, as opposed to just being changed in memory.

Another cool boolean command is togglesebool, which just toggles the boolean, active / inactive.

    :::bash
    ~] togglesebool httpd_enable_cgi
    httpd_enable_cgi: active
    # togglesebool httpd_enable_cgi
    httpd_enable_cgi: inactive

So remember, if you are having issues with SELinux blocking applications like Apache, and all the file contexts are correct, you would next want to look at booleans.
