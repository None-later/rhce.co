Date: 2012-10-06
Title: Install and update software packages from Red Hat Network, a remote repository, or from the local filesystem
Objective: 43
Category: e. Deploy, Configure, and Maintain Systems - (RHCSA)
Tags: RHCSA

Red Hat Network is pretty easy to work with. 

    :::bash
    ~] rhn_register

And follow the instructions. Now, if you arent lucky enough to have a subscription to this wonderful service, then you will most likely using a repo that you create, or that is given to you.

Most common situation is having a remote repository that you need to pull packages from. Usually you be given a url to connect to looking something like this: http://myremote.com/repo/i386/. The yum repo files are located in /etc/yum.repos.d/ and end with a .repo extension. The format is simple to setup a repo on the fly. 

    [myremote]
    name=myremote
    baseurl=http://myremote.com/repo/i386/
    enabled=1
    gpgcheck=0

Those are the essential elements to pull packages via yum from that repo. 

Setting up a local repo with a disk is almost the same with a few steps before. First the disk needs to be mounted, and the packages copied from Packages/ into another directory on the server. In this case we will use file:///directory/path/to/repo/ as the url, where /directory/path/to/repo/ is the directory that contains the rpm files. 

Next the package creatrepo needs to be installed. Once installed cd into the directory and run:

    :::bash
    ~] createrepo .

Now that you have a repo setup, yum needs to know about it. Create a file named mylocal.repo in the /etc/yum.repos.d/ directory. 

    [mylocal]
    name=mylocal
    baseurl=file:///directory/path/to/repo/
    enabled=1
    gpgcheck=0

Run a yum command to test, and it should be pulling information about packages from the local repo.
 
    :::bash
    ~] yum list httpd
