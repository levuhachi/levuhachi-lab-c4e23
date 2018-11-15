a = float(input("a= "))
b = float(input("b= "))
#Warm Up 1:
c = a + b
print("a + b = ",c)
#Warm Up 2:
operation = input("Operation(+,-,*,/: ")
print ("*" * 20)
if operation == "+":
    print("a + b =",a+b)
elif operation == "-":
    print("a - b =",a-b)
elif operation == "*":
    print("a * b =",a*b)
elif operation == "/":
    if b != 0:
        print("a / b =",a/b)
    else:
        print("Oops!")
else:
    print ("Unsupported")


