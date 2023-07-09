''' input and output
we've two types of functions predefined and user defined functions
There's a function called input that defines dynamic print
In python2 they had two functions to capture two values from the keys which was raw input and input   and they discarded one in python3..
In pythhon2 print was just a statement to print however in python3 it is a function
A function is used to capture values from the keysboard.
'''
 

#In python 2.7 we never use the input for the string but we use raw_input
#In python 3 they discarded raw_input and merged it with the input function



#A meaningful functions

def paye(sal,name):
    rate = 0.3
    tax = rate * sal
    netpay = sal - tax
    print("****************************************************************")
    print("Dear: ", name )
    print("Your tax is payable ", tax)
    print("And your take home salary is ", netpay)
    print("................................................................")


print("You're Welcome to our system!") # welcome message    
name = raw_input("Please enter your name: ") #prompting for the name
sal  = float(input("Please enter your salary: ")) #prompting for the sal ...type casting 


paye(sal,name) #calling the function


#Dead code should not be in the code  and should be removed when reguired
#A dead code is a commented out code


#Conditional statements 


