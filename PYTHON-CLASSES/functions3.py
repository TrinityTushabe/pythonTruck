#Afunction is a group of statements that perform a specfic function
#Dynamic functions  or parameterized functions 
#A function that calls returned value  from another function  is called a calling function.
def adding(num1,num2):
    num3 = num1 + num2
    print(num3)

def sub(num1, num2):
    num3 = num1 - num2
    print(num3)
    

 #Forcing the functions to communicate 

def adding1(num1,num2): #num1 and num2 are parameters 
    num3 = num1 + num2
    return num3 # return keeps the function for later 
    print(adding1)

def sub1(num1):
    num3 = adding1(100,79) - num1
    print(num3)  

sub1(5)    # 5 is an argument or or actual parameters or formal parameters 

adding1(2,3) # calling out line 13

ans = adding1(12,13)
print(ans)
print(adding1(2,3))
#When you print a funtion call without a return a value it'll print none 