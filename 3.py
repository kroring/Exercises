# Program to find and display all child files & folders within a given directory
import os
import glob
import sys

#Recursive method 'dirlist' - takes a directoty path
def dirlist(path, c = 1):

        for i in glob.glob(os.path.join(path, "*")):
                if os.path.isfile(i):
                        print '----' *c + os.path.join(i)

                elif os.path.isdir(i):
                        print '----' *c + os.path.join(i)
                        c+=1
                        dirlist(i,c)
                        c-=1

#Wrapper if statements to ensure that only one directory is specified
if len(sys.argv) <= 2:
	if len(sys.argv) >= 2:
                
                path = os.path.normpath(sys.argv[1])

                print ""
                print "Contents of", (os.path.join(path))
                print ""

                dirlist(path)
                
	else:
		print "One directory must be specified - e.g. python 3.py C:\ "
else:
	print "Only one directory can be analysed at a time - e.g. python 3.py C:\ "

