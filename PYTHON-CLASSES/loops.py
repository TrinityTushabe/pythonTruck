'''
A loop helps us to do something repeatedly
for is key word for the begining of a for loop
and is also key word in myCount function
item is any valid name in a loop

'''
#My first loop
def myCount():
    for item in range(10):
        print(item)

myCount()

#my list showing a programing languages  in a for loop  function
#Accessing list elements using a for loop
def list():
    languages = ['python', 'C++', 'javascript', 'c#', 'ruby', 'swift']
    for languages in languages:
        print(languages)

list()   

def example(num):
    for number  in range(num):
        print(number)

example(10)    


#the below function am introduced to the if condition in a loop
def my_lang():
    languages = ['python', 'C++', 'javascript', 'c#', 'ruby', 'swift']
    for language in languages:
        if language == 'python':
            print('Am currently in python class')

my_lang() #envoke  (meaning to call out a defined function)          

def even(num):
    for number in range(num):
        if number % 2 == 0:
            print(number)

even(10)

def power(p):
    my_po = p**2

    if my_po %2 == 0: #the condition is true

        print("The power is an even number")

    else: # the condition is false

        print("The power is an odd number")

power(10)








