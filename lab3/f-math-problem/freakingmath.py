from random import *
from func_intro import eval

def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    error = randint(-2,2)
    op_list = ["+","-","*","/"]
    o = choice(op_list)
    r = eval(x,y,o) + error
    return [x,y,o,r] 

def check_answer(x, y, op, result, user_choice):
    a,b,op,r = generate_quiz()
    print (a,op,b,"=",r)
    ans = input("Y/N: ").upper()
    s = eval(a,b,op)
    if ans == "Y":
        if r == s:
            return True
        if r != s:
            return False
    if ans == "N":
        if r == s:
            return False
        if r != s:
            return True
    pass