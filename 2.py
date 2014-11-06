import sys

#Wrapper if statements to ensure that only one file is specified
if len(sys.argv) <= 2:
	if len(sys.argv) >= 2:
		
		#Read the file to the command line. If something goes wrong, catch the exception and provide feedback to the user.
		try: 
			file = open(sys.argv[1], 'r')
			lines = reversed(file.readlines())
			file.close()
			for line in lines:
				print line.rstrip()[::-1]
		except:
			print 'An error has occurred. Please check that the path is correct, file exists and is of the valid type (.txt)'
		
	else:
		print 'One text file must be speciifed - e.g. python 3.py C:\readme.txt'

else:
	print 'Only one text file can be read at a time - e.g. python 3.py C:\readme.txt'
