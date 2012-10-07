Title: Configure system to authenticate using Kerberos 
Objective: 4
Category: a. System Configuration and Management - (RHCE)
Tags: RHCE

Kerberos is an authentication method that allows users to authenticate without directly providing their password. You can read more on Kerberos over at: 

    http://web.mit.edu/kerberos/

Our goal per the information Provided by Red Hat is to configure a system to authenticate via Kerberos. To begin with we'll need to install openldap-clients, authconfig (usually installed by default).

While we could simply use system-config-authentication that's not really a good real-world example, as I doubt most of your production machines will have a graphical interface.Instead we'll be using authconfig.

authconfig has a long list of options, but the key ones we'll use are: