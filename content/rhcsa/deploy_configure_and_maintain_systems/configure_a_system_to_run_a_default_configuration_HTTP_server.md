Date: 2012-10-06
Title: Configure a system to run a default configuration HTTP server
Objective: 41
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA


Installing apache via yum on Red Hat Enterprise Linux 6 does most of the setup for you. 

    :::bash
    ~]  yum install httpd

    :::bash
    ~]  service httpd start

Now if you try to visit the main ip or domain of the server, you may run into an issue getting to the site. Whenever you enable a network service like a web server, you also have to allow the outside to use that service. We have to add an entry into iptables.

    :::bash
    ~]  iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT

This would add an entry into iptables, but to survive a reboot we would have to save this.

    :::bash
    ~]  service iptables save

Now an easier way of doing this, is to use system-config-firewall, which is the gui/tui tool to configure a firewall. 

    :::bash
    ~]  system-config-firewall

This may not make things perfect, but it can definitely give you a jump start to molding rules on an exam. 

*Tip: it may not be installed by default.*