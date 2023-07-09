def paye(sal,name):
    rate = 0.3
    if sal >= 30000:
        tax = rate * sal
        netpay = sal - tax
        print("****************************************************************")
        print("Dear: ", name )
        print("Your tax is payable ", tax)
        print("And your take home salary is ", netpay)
        print("................................................................")

    else:
        
        print("Dear: ", name)
        print("Your salary is none taxable")


print("You're Welcome to our system!") # welcome message    
name = raw_input("Please enter your name: ") #prompting for the name
sal  = input("Please enter your salary: ") #prompting for the sal ...type casting 


paye(sal,name)