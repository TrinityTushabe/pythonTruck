"""A function  is self-contained i.e  
functions are independent of each other until
you've made them to do otherwise""" 

#Static function for adding 
def add():
    num1, num2 = 3,7
    num3 = num1 + num2
    print(num3)

add() #it gives a static value or hard coded values 


#creating a dynamic function 
def sum(num1,num2):
    num3 = num1 + num2
    print(num3)

sum(17,13)
sum(28,26)

#function for all operators 
def opera(num1,num2):
    num4 = (num1 + num2)
    num5 = (num1 * num2)
    num6 = (num1 % num2)
    num7 = (num1 / num2)
    num8 = (num1 // num2)
    num9 = (num1 - num2)
    num10 = (num1 ** num2)

    print(num4)
    print(num5)
    print(num6)
    print(num7)
    print(num8)
    print(num9)
    print(num10)

opera(9,7)


