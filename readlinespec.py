n=int(input("enter the number of lines:- "))
f=open("hello.txt","r")
for line in (f.readlines()[-n:]):
    print(line, end=" ")

f.close()