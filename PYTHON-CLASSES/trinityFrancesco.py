'''
The defined function takes on two parameters test1 and test2
This function  compares test scores and returns test2 when  they're not equal
test1 (numeric): The first test score to compare.
test2 (numeric): The second test score to compare.
Returns the larger of the two test scores.

'''


def tests(test1, test2):
	#Comparing the two test scores
	if test1 == test2:
		#If they are equal, returns test1
		return test1
	else:
		#Otherwise, returns test2
		return test2
	
#Prompts the user to enter the marks for test1 and test2
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
We're defining the function to calculate the final coursework marks
This function calculates the final coursework marks based on the average of coursework and test scores.
It takes the coursework marks as input and prints the final coursework marks.

'''
def courseWrk(cswork):
	#Calculate the average of the two tests
	testsMark = tests(test1,test2)
	#Calculate the average of the coursework and the tests 
	avgtestsCswork = (cswork + testsMark)/2
	#Calculate the final coursework marks (40% percentage)
	fnltestsCswork = avgtestsCswork * (40/100)
	#This line is used to print a line of dots to visually separate different sections of the program's output. 
	print('..............................')
	# Print the final coursework marks
	print('your final coursework marks is: ', fnltestsCswork)
	#This line is also used to print a line of dots to visually separate different sections of the program's output. 
	print('..............................')

#Prompts the user to enter the coursework marks
cswork = int(input('Please enter your course work Marks: '))
#Call the function to calculate and print the final coursework marks
courseWrk(cswork)

'''

This program calculates the final coursework marks based on the input of test scores and coursework marks.
- The `tests` function compares two test scores and returns the larger score.
- The program prompts the user to input the marks for test1 and test2.
- The `courseWrk` function calculates the average of coursework scores and test scores.
- It then calculates the final coursework marks by multiplying the average by 40%.
- The program prompts the user to input the coursework marks.
- Finally, the `courseWrk` function is called, and the final coursework marks are displayed.

'''