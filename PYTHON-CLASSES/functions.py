#functions refer to  grouped statements

num1 = 20
num2 = 100
num3 = num1 + num2
print(num3)

# introducing defining function 
#add
def sum():
    num1,  num2  = 50, 100
    num3 = num1 + num2
    print(num3)

sum()

#substraction
def sub():
    num1, num2 = 900,  1000
    num3 = num2 - num1
    print(num3)

sub() 

#div for a rema
def rem():
    num1, num2 = 6, 5
    num3 = num1%num2
    print(num3)

rem()    # Here am calling the function above  defined as rem

#A named group of statements is called a function

#lists in Functions
def mylist():
    mylist = [1,2,3,4,5,6,7,8,9]
    print(mylist[5])

mylist()  

# the above parameters are called static parameters 
    
    