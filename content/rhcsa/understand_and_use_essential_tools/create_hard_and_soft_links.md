Date: 2012-10-06
Title: Create hard and soft links
Objective: 09
Category: a. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA


Hard Links
===

A *hard link* is a link where two files are really the same file. 

Watch how when we create a file, and link to it with a hard link, the inodes (exact location on the harddisk) are the same.

    ::bash
    $ touch file.txt
    $ ln file.txt file1.txt
    $ ls -li file*
    524594 -rw-r--r--. 2 root root 0 Mar 21 12:54 file1.txt
    524594 -rw-r--r--. 2 root root 0 Mar 21 12:54 file.txt
 

When we create a third file linking it to the original, we see the same thing. They all are have an inode of 524594. 

    ::bash
    $ ln file.txt file2.txt
    $ ls -li file*
    524594 -rw-r--r--. 3 root root 0 Mar 21 12:54 file1.txt
    524594 -rw-r--r--. 3 root root 0 Mar 21 12:54 file2.txt
    524594 -rw-r--r--. 3 root root 0 Mar 21 12:54 file.txt


What happens if we delete the original file?

    ::bash    
    $ rm file.txt
    rm: remove regular empty file 'file.txt'? y
    $ ls -li file*
    524594 -rw-r--r--. 2 root root 0 Mar 21 12:54 file1.txt
    524594 -rw-r--r--. 2 root root 0 Mar 21 12:54 file2.txt
 
As you can see, the other two files are in tact and have not been removed, even though the original file is gone. That is because they are all the same file, when you make a hard link to it you are just putting another reference to it with a different name. Until the last file with that inode gets deleted, that file lives on.

Lets put some text in file2.txt and see what happens
 
    ::bash
    $ echo "things" >> file2.txt
    $ ls -li file*
    524594 -rw-r--r--. 2 root root 7 Mar 21 13:01 file1.txt
    524594 -rw-r--r--. 2 root root 7 Mar 21 13:01 file2.txt
    $ cat file1.txt 
    things
    $ cat file2.txt 
    things

As you can see, the files both grew to 7 bytes, and when we look inside each one, they both have the same text. That's because they are the same.

Soft Links
===

A *soft link* is much different from a hard link. Most people relate hard links to shortcuts in Windows. When you put a shortcut on your Desktop, it is just a link to the something on your computer. If you delete it no biggie, its just a link. Soft links are the same way. 

    ::bash
    $ touch testfile.txt
    $ ln -s testfile.txt testfile1.txt
    $ ls -li testfile*
    524726 lrwxrwxrwx. 1 root root 12 Mar 21 13:11 testfile1.txt -> testfile.txt
    524725 -rw-r--r--. 1 root root  0 Mar 21 13:11 testfile.txt


Here we created a file, testfile.txt, and then ran `ln -s` to create a soft link. When we ran `ls -li` we see that now the inodes are different, and testfile1.txt shows highlighted with an arrow to testfile.txt.

OK, so now lets repeat what we did above for hard links. I will make another soft link, linking to the original file testfile.txt and call it testfile2.txt. Then I'll delete the original and `ls -li`
 
    ::bash
    $ ln -s testfile.txt testfile2.txt
    $ ls -li testfile*
    524726 lrwxrwxrwx. 1 root root 12 Mar 21 13:11 testfile1.txt -> testfile.txt
    524727 lrwxrwxrwx. 1 root root 12 Mar 21 13:15 testfile2.txt -> testfile.txt
    524725 -rw-r--r--. 1 root root  0 Mar 21 13:11 testfile.txt
    $ rm testfile.txt 
    rm: remove regular empty file 'testfile.txt'? y
    $ ls -li testfile*
    524726 lrwxrwxrwx. 1 root root 12 Mar 21 13:11 testfile1.txt -> testfile.txt # Imagine RED here
    524727 lrwxrwxrwx. 1 root root 12 Mar 21 13:15 testfile2.txt -> testfile.txt # Imagine RED here

If we try and cat the two files, to see the contents, we get an error. We can no longer access these files, they are broken links. 

    ::bash
    $ cat testfile*
    cat: testfile1.txt: No such file or directory
    cat: testfile2.txt: No such file or directory

