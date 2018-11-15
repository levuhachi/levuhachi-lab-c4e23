from random import randint,choice
def add(a,b): 
    r = a + b
    return r

# Call Function
# s = add(7,8) # Thay a va b
# print(s)

# Write a function named "eval" receiving 3 function parameters - a,b,op
# From a,b,op. Find result and return it and use it

# Write function
def eval(a,b,op):
    if op == "+":
        c = a + b
    elif op == "-":
        c = a - b
    elif op == "*":
        c = a * b
    elif op == "/":
        if b != 0: 
            c = a / b
    return c

# Print and Use result
# s = eval(2,1,"/")
# print (s)
def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    error = randint(-2,2)
    op_list = ["+","-","*","/"]
    o = choice(op_list)
    r = eval(x,y,o) + error
    return x,y,o,r 