Date: 2012-10-06
Title: Diagnose and correct file permission problems
Objective: 32
Category: d. Create and Configure File Systems - (RHCSA)
Tags: RHCSA

Filesystem permssions can be diagnosed best with the ls -l option, which will display the permission bits on the file. 

    ~]$ cat rootfile.txt 
    cat: rootfile.txt: Permission denied

A typical filesystem permission issue will look like the above. With a permission denied error. 

    ~] ls -l rootfile.txt 
    -rwxrwx---. 1 root it 0 Apr 14 01:32 rootfile.txt

Permission denied can show up in log files as well, example being the apache error log.
