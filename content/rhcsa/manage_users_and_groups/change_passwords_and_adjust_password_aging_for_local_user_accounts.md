Date: 2012-10-06
Title: Change passwords and adjust password aging for local user accounts
Objective: 47
Category: f. Manage Users and Groups - (RHCSA)
Tags: RHCSA

The utility used for password aging is chage. As with most unix tools, its name sounds like a short lazy of saying the action... in this case, "change age".

The switches are everything here, and unless you use this all the time, the man page will be in order here. For now, here are the options:

    -m <days   Specifies the minimum number of days between which the user must change passwords. If the value is 0, the password does not expire.
    -M <days>  Specifies the maximum number of days for which the password is valid. When the number of days specified by this option plus the number of days specified with the -d option is less than the current day, the user must change passwords before using the account.
    -d <days>  Specifies the number of days since January 1, 1970 the password was changed
    -I <days>  Specifies the number of inactive days after the password expiration before locking the account. If the value is 0, the account is not locked after the password expires.
    -E <date>  Specifies the date on which the account is locked, in the format YYYY-MM-DD. Instead of the date, the number of days since January 1, 1970 can also be used.
    -W <days>  Specifies the number of days before the password expiration date to warn the user.

Examples:
 
List a users passowrd expiration info

    :::bash
    ~] chage --list username

Set an expiration based on a maximum number of days for which the password should be valid.

    :::bash
    ~] chage -M 120 username

To only allow a user to change their password every 10 days, and no more

    :::bash
    ~] chage -m 10 username

Apply immediate expiration

    :::bash
    ~] chage -d 0 username
