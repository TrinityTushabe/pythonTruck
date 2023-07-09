def paye(sal, name, age, occupation, location):
    rate = 0.3
    if sal >= 30000:
        tax = rate * sal
        netpay = sal - tax
        print("****************************************************************")
        print("Dear:", name)
        print("Age:", age)
        print("Occupation:", occupation)
        print("Location:", location)
        print("Your tax is payable:", tax)
        print("And your take home salary is:", netpay)
        print("................................................................")
    else:
        print("****************************************************************")
        print("Dear:", name)
        print("Age:", age)
        print("Occupation:", occupation)
        print("Location:", location)
        print("Your salary is non-taxable")
        print("................................................................")

print("Welcome to our system!")  # welcome message
name = raw_input("Please enter your name: ")  # prompting for the name
birth_year = input("Please enter your year of birth: ")  # prompting for the year of birth
occupation = raw_input("Please enter your occupation: ")  # prompting for the occupation
location = raw_input("Please enter your location: ")  # prompting for the location
age = 2023 - int(birth_year)  # calculate the age based on the birth year
sal = float(raw_input("Please enter your salary: "))  # prompting for the salary

paye(sal, name, age, occupation, location)
