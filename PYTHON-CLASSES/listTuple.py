#List Tuple and Dictionary(dict) in details 
#A list is a mutable datatype
'''
Multi line comments
Do not write multi-line functions within the functions
We have single line comments(#) and multi-line comments('''''')
Endeavour always to put comments in your code.
'''
#mylist starts here
def mylist():
    #declaring my list 
    #my single line comment & can be written within a function
    mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(mylist[5])
    mylist2 = [10, 20, 30, 40, 50]
    print(mylist2[4])
    print(mylist2[-1])
    print(mylist2[-2])

mylist() 


'''
comment again
we write muti-line comments in functions
'''

#My osman function starts here
def osman():
    osman = [100, [200]]
    print(osman[1][0])

    #example of mutable list
    osman.append(1000)
    osman.pop()
    print(osman)

osman() 


#My fruits list function starts here 
def fruits():
    fruits = ['orange', 'apple', 'pineapple']
    fruits.append('fene')
    print(fruits)
    fruits.pop()
    print(fruits)

fruits()
   

#My osman2 list function starts here
def osman2():
    osman2 = [1000, [[2000,3000]]]
    print(osman2[1][0][1])

osman2()


#Tuples in details
#A tuple is an immutable datatype

#My function for tuple starts here 
def myTuple():
    myTuple = (10,20,30,40,50)
    print(myTuple)

myTuple()




#dictionary (dict )
#braces are identified using {} these are mutable

#My function for dict starts here 
def zeb():
    zebra = {'name':'tongs', 'legs': 4, 'color':'black & white', 'Sex':'male'}
    print(zebra.keys())
    print(zebra.values())
    print(zebra)
    zebra.__delitem__('name')
    print(zebra)
zeb()
