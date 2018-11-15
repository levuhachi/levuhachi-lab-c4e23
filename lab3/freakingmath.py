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
    #a,b,op,r = generate_quiz()
    print (x,op,y,"=",result)
    s = eval(x,y,op)
    if user_choice is True:
        if result == s:
            return True
        if result != s:
            return False
    if user_choice is False:
        if result == s:
            return False
        if result != s:
            return True
    pass