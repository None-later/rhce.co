Date: 2012-10-06
Title: Create and configure set-GID directories for collaboration
Objective: 30
Category: d. Create and Configure File Systems - (RHCSA)
Tags: RHCSA

Set-GID directories are used for group collaboration. Everything that is created in a directory with that special permission bit, is automatically owned by the group. 

To set that permission bit you have to add one more digit than you usually see to permission sets, or another character depending on how to usually set permissions. 

The *digit-based way* to setup a set-GID directory:

We start off with a directory under root, named share. Right now its owned by root, along with everything under it. 

    :::bash
    ~] ls -l | grep share
    drwxr-xr-x.   2 root root  4096 Apr  6 10:28 share

    ~] ls -l share/
    total 0
    -rw-r--r--. 1 root root 0 Apr  6 10:28 file213

First step in this process is changing group ownership of the directory to the group. 'it' will be the group in this example. 

    :::bash
    ~] chgrp -R it  share/

    ~] ls -l share/
    total 0
    -rw-r--r--. 1 root it 0 Apr  6 10:28 file213

As you can see, we recursivley change the directory and contents to the 'it' group, but its still owned by root. 
Next we would apply the set-gid permission on the directory by adding a 2 before the standard permissions set. 

    :::bash
    ~] chmod 2755 share/

    ~] ls -l | grep share
    drwxr-sr-x.   2 root it    4096 Apr  6 10:28 share

Now you can see the directory has a permission set that contains an 's' now in place of the x for group. Lets test this out. I am going to touch a file as root in this directory. 

    :::bash
    ~] touch newfile
    ~] chmod 760 newfile
    ~] ls -l
    total 0
    -rw-r--r--. 1 root it 0 Apr  6 10:28 file213
    -rwxrw----. 1 root it 0 Apr 13 02:03 newfile

So you can see that automatically a group ownership is added to this file, which means anyone in the group 'it' can now read and write to this file, while anyone else cannot.


The *character-based way* to setup a set-GID directory:

The only thing done differently with this method is the way the permissions are set. Instead of numerical/digit permissions, we use letters. First we list the permissions.

    :::bash
    ~] ls -l | grep share
    drwxr-xr-x.   2 root it    4096 Apr 13 02:03 share

Then apply the permissions with g+s, for group plus set-guid bit.
  
    :::bash
    ~] chmod g+s share/

    ~] ls -l | grep share
    drwxr-sr-x.   2 root it    4096 Apr 13 02:03 share

As you can see it has the same effect, just a different approach.
