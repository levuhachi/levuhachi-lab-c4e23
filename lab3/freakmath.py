from random import randint
a = randint(0,10)
b = randint(0,10)
error = randint(-2,2)
r = a + b + error
print (a,"+", b, "=",r)
ans = input("Y/N: ").upper()
# Way 1:
if error == 0 and ans == "Y":
    print("Passed")
elif error == 0 and ans == "N":
    print("Over")
elif error != 0 and ans == "Y":
    print("Over")
elif error != 0 and ans == "N":
    print("Passed")
# Way 2:
c = a + b
if c == r and ans == "Y":
    print("Passed")
elif c == r and ans == "N":
    print("Over")
elif c != r and ans == "Y":
    print("Over")
elif c != r and ans == "N":
    print("Passed")

