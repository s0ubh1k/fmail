
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
        self.users[username] = password


x = auth()
x.readCredFile()
x.add("FFF", "FFF")
print(x.login("Soubhik", "xxxxxxxxxxxxxxxxxxxx"))

x.writeCredFile()
