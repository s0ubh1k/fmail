a = open("credentials" , 'r+')

def add_(user,pass_d):
    x=open("credentials" , "a+")
    x.write(user+":")
    x.write(pass_d+"\n")
    x.close()

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
def 

user=input("Enter your name: ")
pass_d=input("Enter your password: ")
add_(user , pass_d)
