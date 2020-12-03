from fabric.api import *

'''
OPS435 Assignment 2S - Fall 2020
Program: a2r_mkobzar.py
Author: Maxim Kobzar
The python code in this file a2s_mkobzar.py is original work written by
Maxim Kobzar. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
'''

env.user = "student"


def addUser(name):
    '''add a user with given user name to remote system'''
    ...


def listUser():
    '''return a list of shell user on a remote system'''
    ...

    # open file and save to list
    f = open("/etc/passwd")
    lines = f.readlines()
    print(lines)

    # test for shell user in list
    shell_user = []
    for line in lines:
        if line.count("/bin/bash") != 0:
            shell_user.append(line)
    print(shell_user)
    
    # split user info by colon
    parsed_user = []
    for item in shell_user:
        parsed_user.append(item.split(":"))
    print(parsed_user)
    
    # create list of names of users
    name_user = []
    for user in parsed_user:
        name_user.append(user[0])
    print(name_user)
    

def listSysUser():
    '''return a list of system (non-shell) user'''
    ...

    # open file and save to list
    f = open("/etc/passwd")
    lines = f.readlines()
    print(lines)

    # test for sys user in list
    sys_user = []
    for line in lines:
        if line.count("/sbin/nologin") != 0:
            sys_user.append(line)
    print(sys_user)
    
    # split user info by colon
    parsed_user = []
    for item in shell_user:
        parsed_user.append(item.split(":"))
    print(parsed_user)
    
    # create list of names of users
    name_user = []
    for user in parsed_user:
        name_user.append(user[0])
    print(name_user)



def findUser(name):
    '''find user with a given user name'''
    ...