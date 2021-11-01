a = open("credentials" , '+r')
def add():
    user=input("Enter your name")
    pass_d=input("Enter yout Password")
    a=open("credentials" , +w)
    a.write(user , ":")
    a.write(pass_d)
    a.close()
def login(user , pass_d):
    
    x = a.read()
    lines = x.split("\n")
    for line in lines:
        y = line.split(":")
        print(y)
        if user == y[0] and pass_d == y[1]:
            print("Logged In!")
            
            return True
        
    print("No such user")
    return False

user=input("Enter your name: ")
pass_d=input("Enter your password: ")
login(user , pass_d)
