from random import randint,choice
from func_intro import eval,generate_quiz

a,b,op,r = generate_quiz()
print (a,op,b,"=",r)
ans = input("Y/N: ").upper()
s = eval(a,b,op)
if r == s:
    if ans == "Y":
        print ("Right")
    if ans == "N":
        print ("Wrong")
if r != s:
    if ans == "N":
        print ("Right")
    if ans == "Y":
        print ("Wrong")