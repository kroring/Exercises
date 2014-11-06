#Application to list all .gif & .jpeg image links from provided URL
#Import required packages
import re, urllib, urllib2, os, sys
from urlparse import urljoin

#If parameter has been given, set URL value to that
if len(sys.argv) >= 2:
    URL = sys.argv[1]
#Promp the user for a URL if none has been provided
else:
    #Prompt the user for a URL
    URL = raw_input("Please enter a web-site URL (e.g. www.rte.ie) to download gif and jpeg images from: ")


#Ensure a URL has been provided before proceeding
if URL:
    
    URL = "http://" + URL
    
    #Open the URL
    try: 
        
        #Set response object to the open URL
        response = urllib2.urlopen(URL) 
        
        #Retrieve all .gif & .jpeg image links from provided URL and store in array object called links
        links = re.findall('[a-zA-Z0-9$-_@.&+!*\(\),]+\.(?:gif|jpeg|jpg)', response.read(), re.I)
    
        #Close the connection
        response.close()
        
    #If a problem occurs e.g. web-site is unreachable, provide user friendly feedback
    except urllib2.URLError, e:
        print ""
        sys.exit("Web-site is unreachable please ensure the URL you are trying to download images from valid and currently live  - e.g. www.rte.ie")
        
    #If array has items...
    if links:

        #Let user know where files are being downloaded to (current working directory in this case)
        print ""
        print "Downloading images to: " + os.getcwd()
        print ""

        #Loop through array of links - downloading one on each iteration
        for link in links:
            
            #Make relative paths absolute
            link = urljoin(URL, link)
            
            #Download the file - maintaining the filename & extension
            urllib.URLopener().retrieve(link, link.split("/")[-1])
            
            #Print status
            print link.split("/")[-1] + " :: [Download Complete]"

    #If array doesn't have items
    else:
        print "No images of type .GIF, .PNG or .JPG found at " + URL
        
else:
    print ""
    print "Valid web-site URL required to download images from - e.g. www.rte.ie"