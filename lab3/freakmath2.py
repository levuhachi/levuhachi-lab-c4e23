from random import randint,choice

op_list = ["+","-","*","/"]
op = choice(op_list)
error_list = [-1,0,1]
error = choice(error_list)

a = randint(0,10)
b = randint(0,10)

t = a + b + error
h = a - b + error
n = a * b + error
c = a / b + error

ans_list = [t,h,c,n]
show_ans = [(a,"+",b,"="),(a,"-",b,"="),(a,"*",b,"="),(a,"/",b,"=")]
for l in ans_list:
    
    print (choice(ans_list))
ans = input("Y/N: ").upper()
if error == 0 and ans == "Y":
    print("Passed")
elif error == 0 and ans == "N":
    print("Over")
elif error != 0 and ans == "Y":
    print("Over")
elif error != 0 and ans == "N":
    print("Passed")
