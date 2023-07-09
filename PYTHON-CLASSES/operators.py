#operators in python
#operators tell a computer what to do with an operand
#operand is what an operator acts upon
#These operators are categorised.
#Arithmetic operators (+, -, *, / ,//,%,$,**)
#examples 
num = 10
num2 = 20
print(num + num2)
print(num - num2)
print(num * num2)
print(num / num2)
print(num // num2)
print(num ** num2)
print(num % num2)

#Assignment operators (=, +=, -=, *=, /=, %=, //=, **=)
num3 = 50
num4 = 100
num3 += num4 # get and add the two values (same as num3 = num3 + num4)
print(num3)
num3 -= num4
print(num3)

#comparison operators we compare with == (!=, <, >, >=, <=,)
print(num == num4)
print(num != num4)
print(num < num4)
print(num <= num4)

#logical operators (and, or , not)
print(True and True)
print(True and False)
print(False and False)
print (True or False)
print(not True)

#identity operators (is, is not)
name = "Claire"
print(num3 is num4) 
print(num3 is not num4)

#membership operators (in and not in)
print("a" in  name)
print("o" in  name)
print("A" in  name)
print("o" not in name)



 
