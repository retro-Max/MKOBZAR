
def fileOpen():
    '''test
    '''
    #open file and save to list
    f = open("/etc/passwd")
    lines = f.readlines()
    return lines


def getShell(lines):
    #test for shell user in list
    shell_user = []
    for line in lines:  
        if line.count("/bin/bash") !=0:
            shell_user.append(line)
    return shell_user


def parseUsers(shell_user):
    #split user info by colon
    parsed_user = []
    for item in shell_user:
        parsed_user.append(item.split(":"))
    return parsed_user 
    

def outUser(parsed_user):
    #create list of names of users
    name_user = []
    for user in parsed_user:
        name_user.append(user[0])
    return name_user  
