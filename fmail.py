a = open("credentials" , 'r+')
def add():
    user=input("Enter your name")
    pass_d=input("Enter yout Password")
    a=open("credentials" , "+w")
    a.write(user , ":")
    a.write(pass_d+"\n")
    a.close()
<<<<<<< HEAD
add(user,pass_d)
=======

>>>>>>> a70335fd90c6c9392db69a182b190b93d637da82
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
