Date: 2012-10-06
Title: Create, delete and modify local groups and group memberships
Objective: 48
Category: f. Manage Users and Groups - (RHCSA)
Tags: RHCSA

Working with groups is a lot like working with users. Commands include groupadd, groupmod, groupdel, groups

Examples:

*List the groups a user is in*
--
    :::bash
    ~]  groups username
    username : username wheel sales

*Add a group*
--

    :::bash
    ~]  groupadd sales

*Delete a group*
--

    :::bash
    ~]  groupdel sales

*Modify a group's name*
--

    :::bash
    ~]  groupmod -n salesfolk sales

*Modify a group's GID*
--

    :::bash
    ~]  groupmod -g 217 sales

*Delete a group*
--

    :::bash
    ~]  groupdel sales

*Add user bob to sales*
--

    :::bash
    ~]  groupmems -g sales -a bob
