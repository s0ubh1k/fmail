def logedin_menu(user_name ):
    print("Welcome " + user_name)
    print("1. change password \n 2. Delete")
    
    opt = input("Enter your choise: ")
    if opt == "1":

        cr_pr=input(" Current password: ")
        nw_pr=input("New Password: ")
        if x.chg_pass(user_name, cr_pr,nw_pr) == True:
            print("Your password changed")
        else:
            print("You have entered Wrong Password")
    if opt == "2":
        user_name=input(" Username: ")
        cr_pr=input("password: ")
        if x.del_user( user_name , cr_pr) == True:
            print("User deleted")
        else:
            print("Wrong password")
       

class auth:
    def __init__(self):
        self.users={}
    def readCredFile(self):
        creadFile = open("cred")
        for userL in creadFile.readlines():
            userL = userL.replace('\n', '')
            user = userL.split(":")
            self.users[user[0]] = user[1]

    def writeCredFile(self):
        credFile = open('cred', "w+")
        users_array = []
        for user in self.users.keys():
            users_array.append(user+":"+self.users[user])
        user_data = "\n".join(users_array)
        credFile.write(user_data)
        credFile.close()
    
    def login(self, username, password):
        if username in self.users.keys():
            if password == self.users[username]:
                return True
            else: return False
        else: return False  

    
    def add(self, username, password):
        
        if not username in self.users.keys():
            self.users[username] = password
            self.writeCredFile()
            return True
        else: 
            return False
    def chg_pass(self , username , password , new_password):
        if not self.login(username,password):
           
            return False
        else:
            self.users[username] = new_password
            self.writeCredFile()
            return True
    def del_user(self , username , password):
        if self.login(username , password):
            self.users.pop(username)
            return True
        else:
            return False

    



x = auth()
x.readCredFile()
option=input("1-Login \n 2-Create user: ")
user_name=input("Enter username: ")
pass_d=input("Current password: ")
if option == "1":
    
    if x.login(user_name , pass_d) == True:
        print("Logged in")
        logedin_menu(user_name)

    else:
        print("Username or password is incorrect")
if option == "2":
    if x.add(user_name , pass_d)==True:

        
        print("New user added")
        logedin_menu(user_name)
    else:
        print("Username already exists")
    
        

