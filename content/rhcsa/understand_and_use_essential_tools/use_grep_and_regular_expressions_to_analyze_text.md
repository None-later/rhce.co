Date: 2012-10-06
Title: Use grep and regular expressions to analyze text
Objective: 03
Category: 1. Understand and Use Essential Tools - (RHCSA)
Tags: RHCSA


RHCSA requirements state that you must know how to use grep to analyze text. This is actually going to be pretty necessary to do many administration tasks on a daily basis.

Grep returns any lines that have characters, words, or expressions that match your query.

Basic usage examples of this include:

Find "Permission Denied" entries in a log file

    :::bash    
    $ grep -r "Permission Denied" /path/to/logfile/

Find "Permission Denied" entries in a log file by using output redirection

    :::bash
    $ cat /path/to/file/ | grep "Permission Denied"

Check out some grep examples at : http://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/[http://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/]

To see all the options check out the Unix Man page, http://unixhelp.ed.ac.uk/CGI/man-cgi?grep[http://unixhelp.ed.ac.uk/CGI/man-cgi?grep] also available by just plain typing <code>man grep</code>