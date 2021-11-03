from simple_term_menu import TerminalMenu
def logedin_menu(user_name ):

    print("Welcome " + user_name)
    options = ("Compose mail " , "Settings" ) 
    terminal_menu = TerminalMenu(options)
    option = terminal_menu.show()
    if option == 0:
        to = input("To whome: ")
        subject = input("Subject: ")
        body = input("Body: ")
        exit
    if option == 1:
        options = ("See Personal Details " , "Delete account" ) 
    terminal_menu = TerminalMenu(options)
    option = terminal_menu.show()
    if option == 0:
        print("Halklo")
    if option == 1:
        pass_d = input("Enter Password")
        if x.del_user(user_name , pass_d) == True:
            print("User Deleted")
        else :
            print("wrong password")
            


        
            







    
    
   
        
       

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
option=["Login"  ,"Create user: "]
terminal_menu = TerminalMenu(option)
option = terminal_menu.show()
 
if option == 0:
    user_name=input("Enter username")
    pass_d = input("Enter Password")
    if x.login(user_name , pass_d) == True:
        logedin_menu(user_name)

    
        

