#data types refers to categorising of values stored in a memory  or the grouping of data ... it's the way of storing values to   a given  memory space
#different categorise of data types(examples numerics, string, sequence, mapping, boolean, set, ) 
#Numerics(int, float, complex)

num1 = 1000
num2 = 1000.0
num3 = 0
num4 = 1 + 2j
name = "Claire"
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))

#string(str) any value in "" or '' is a string
num5 = "1000"
print(type(num5))
print(type(name))

#sequence(list, turple, range)
myList = [0, 2, 4, 6, 8, 10]
myList2 = [0, 2, 4, 6, "Claire",10.5]
print(type(myList))
print(type(myList2))


#Tuple 
myTuple =  (0,2,4,6)
print(type(myTuple))

#Mapping (dict)
my_dict = {'Uganda': 'Kampala', 'Italy' : 'Rome' , 'Frances' : 'Paris', 'Tanzania' : 'Dodoma' }
print(type(my_dict))

#Booleans(True or False)

#set ()
mySet = {0,5, 10 ,15, 20}
print(mySet)
mySet2 = {5,5,10,10,15,15,20,20}
print(mySet2)
print(set(my_dict))

