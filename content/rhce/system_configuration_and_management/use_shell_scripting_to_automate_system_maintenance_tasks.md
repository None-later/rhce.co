Date: 2012-10-06
Title: Use shell scripting to automate system maintenance tasks
Objective: 7
Category: a. System Configuration and Management - (RHCE)
Tags: RHCE

It is important to be familiar with basic bash scripting. Some commands were covered in the RHCSA portion, however writing scripts was not. Lets look at writing some basic scripts.

The most important thing we need to start with is our shebang:

    :::bash
    #!/bin/bash

The shebang is used to invoke the proper interpreter. You can read more about the shebang itself here: http://en.wikipedia.org/wiki/Shebang_%28Unix%29 for now however, we're not going to discuss it further. Just make sure it's at the top of your shell script.

As with most scripting languages, a key concept to understand is variables. This is no difference in bash scripting, lets look at an example of a variable, how to assign a value, and how to return that value using echo:


    :::bash
    ~] OPERATINGSYSTEM=rhel6
    ~] echo $OPERATINGSYSTEM
    rhel6
    ~] echo OPERATINGSYSTEM
    OPERATINGSYSTEM
    ~] os=rhel6
    ~] echo $os
    rhel6


As you can see, we've declared our variable, and given it a value, and returned that value. Notice we needed the $ to ensure that it was referenced as a variable. If you don't use $NAME the interpreter will just use the literal value of whatever the variable's name is, which is bad news. Additionally you can see that the case of the variable doesn't matter. Obviously you should practice good variable naming conventions, but that won't be covered here.

While we're discussing the use of echo, lets review the use of quoting,
