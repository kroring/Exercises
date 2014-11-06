#Function to randomly pick a number between any two given numbers passed as params when running program
import random
import sys

#Wrapper if statements to ensure no less/more than two parameters have been passed
if len(sys.argv) <= 3:
	if len(sys.argv) >= 3:
	
                #Try/Except block used in case two whole numbers aren't passed (used here to cut down lines of code)
                try:
                        parameter_1 = int(sys.argv[1])
                        parameter_2 = int(sys.argv[2])

                        #Swap numbers if the first parameter is bigger than the other because the 'randint' function requires the
                        #first number to be smaller than the second
                        if parameter_1 > parameter_2:
                                temp = int(parameter_1)
                                parameter_1 = parameter_2
                                parameter_2 = temp	
                        print random.randint(parameter_1,parameter_2)

                except:
                        print 'Only whole numbers are accepted - e.g. python 1.py 1 400'
	else:
		print 'Please pass two parameters only - e.g. python 1.py 1 400'
else:
    print 'Please pass two parameters only - e.g. python 1.py 1 400'


    
