a = open("credentials" , 'r+')

def add_(user_,pass_d):
    a=open("credentials" , "+w")
    a.write(user+":")
    a.write(pass_d+"\n")
    a.close()

