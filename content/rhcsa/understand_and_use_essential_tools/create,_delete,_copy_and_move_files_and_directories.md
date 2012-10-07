Date: 2012-10-06
Title: Create, delete, copy and move files and directories
Objective: 08
Category: 1. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA

''Objective: Create, delete, copy and move files and directories''

Administering a system requires moving, copying, and deleting files and directories. These are tasks that you will encounter on a constant basis and are essential to the RHCE.

Some of the most important commands are the ones that we will list below. 


<b>ls</b> - List contents of a directory
--

    :::bash
    # list the contents of the home directory.
    $ ls /home/ 
 

<b>cp</b> - Copy a file or group of files to another location on the machine.
--

    ::bash
    # copy file1 as file2
    cp file1 file2 
     

<b>mv</b> - Move a file or directory 
--

    ::bash
    # move a directory to the /tmp directory
    $ mv directory /tmp/
    
 

<b>cd</b> - Change directory
--

    ::bash
    # navigate into the /home/ directory
    $ cd /home/   
    
    # navigate from home into the /etc directory, using the .. to reverse out of the directory
    $ cd ../etc/  
    

<b>rm</b> - remove files or directories. 
--

    ::bash
    # remove file1
    $ rm file1  

    # remove directory with all contents (Caution when using this!)
    $ rm -rf directory1/ 
    
 

<b>touch</b> - create a new blank file
--

    ::bash
    # create a blank file named myfile.txt
    $ touch myfile.txt 
    
<b>mkdir</b> - create a new directory
--

    ::bash
    # create a directory in the present working directory
    $ mkdir directory1  
    


<b>pwd</b> - Get the present working directory
--

    ::bash
    # find the present working directory. Handy when you need to see where in the system you are.
    $ pwd     
    $ /home/david/ 
    
 

<b>head</b>- Display first lines of a file, default to 10 lines
--

    ::bash
    # display the first 10 lines of file1
    head file1
    
    ::bash
    # display the first 50 lines of file1
    head -50 file1
    
 

<b>tail</b> -Display last lines of a file, default to 10 lines
---

    ::bash
    # display the last 10 lines of file1
    tail file1 
    
    # display the last 50 lines of file1   
    tail -50 file1   
    
 
