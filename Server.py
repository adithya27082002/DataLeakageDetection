#server
import socket
import random
alpha=["code1","code2","code3","code4","code5"]
num=[1,2,3,4,5]
sym=["@","#","%","!","*"]
s=socket.socket()
print("Server Created!")
s.bind(('localhost',9999))
s.listen(3)
print("Enter data: ")
str1=input()
if(str1.isdigit()):
    new_data=str1+str(random.choice(num))
elif(str1.isalpha()):
    new_data=str1+random.choice(alpha)
elif(str1.isalnum()):
    new_data=str1+random.choice(sym)+random.choice(sym)
#print("The data which will be sent is: ",new_data)
print("Waiting for connection...")
while True:
    c,addr=s.accept()
    print("Server connected with addr: ",addr)
    print("The data sent is:",new_data)
    c.send(new_data.encode('ascii'))
    print("The time is printed on the client side.")
    c.close()



