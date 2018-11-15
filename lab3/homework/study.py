# 1.Why should we use functions at all?
    # Reusability - we can reuse it in our programs without coding the same long things once again
    # Easy-to-read - as we can reuse the functions, our programs can be shortened 
        # --> easy to test and read code
    # Flexibility - just need to make change in one place and one time, then everywhere we use functions, it will be automatically changed
    # Accessibility - everyone can use without knowing how to code that functions - it's such a standard library
# 2.How to define/declare a function?
    # Step 1: Declare the function using:
        #  def function_name (parameters)
    # Step 2: Add the program statements to be executed.
# 3.How to call/use a function?
    #Write the name of function, with parameters inside (if have)
    # For example:
        # function_name()
        # or function_name(1,2) (if the function_name has two interger arguments)
# 4.What is return, why and how do we use it?
    # Return is used to make the expression in function exist and hand back values to the caller
    # We use it by writing:
        # return <name of expression we want to save and reply to the caller> 
            #each "return" used for each expression
     
# 5.Do we have to use return in every function?
    # No. In case, the function is not executed for its resulting value, but for some other reasons
    # If the programmer doesn’t arrange to return a value, Python will automatically return the value None

# 6.What are function arguments/parameters, why and how we use it?
    # function arguments/parameters are local variables that can be used only insde the function
    # we use it to execute program inside the function
    # how we use it (get back to question number 2 and 3)

# 7.How to use function from a different file other than our currently working file?
    # we just need to call the name of file that holding the function then import the function
    # from <name of file> import <function>

