Date: 2012-10-06
Title: Configure a system to use an existing LDAP directory service for user and group information
Objective: 49
Category: f. Manage Users and Groups - (RHCSA)
Tags: RHCSA

    :::bash
    ~]  yum -y install openldap-clients system-config-authentication

    ~]  system-config-authentication

Check enable ldap support. Then configure should open up a windows that allows you to just add the ldap info, and be done. Not much too this objective, seeming as you only have to be able to connect and authenticate.
