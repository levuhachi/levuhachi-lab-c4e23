content = "Treasure"

with open("content.txt","r") as f:
    c = f.readlines() 
    # c = f.read()
    print(c)
# #1. Open file
# f = open("content.txt","w") #write

# #2. Write file
# f.write(content)
# f.write("hihi") 

# #3. Close file
# f.close()