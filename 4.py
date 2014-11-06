#Import required packages
import urllib2, sys

#If parameter has been given, set URL value to that
if len(sys.argv) >= 2:
    URL = sys.argv[1]
#Promp the user for a URL if none has been provided
else:
    #Prompt the user for a URL
    URL = raw_input("Please enter a web-site URL (e.g. www.rte.ie) to analyse header information: ")


#Ensure a URL has been provided before proceeding
if URL:
    
    #Append required http:// for urllib3.urlopen to work
    if(not URL.startswith('http://')):
        URL = "http://" + URL
    
    #Open the URL
    try:
        
        #Set response object to the open URL
        response = urllib2.urlopen(URL) 
        
        print ""
        print "Header parameters returned from", URL, ":"
        print ""
            
        #Print given web-siteheaders to console
        print response.info()

        #Close the connection
        response.close()
    
    #If a problem occurs e.g. web-site is unreachable, provide user friendly feedback
    except urllib2.URLError, e:
        print ""
        print "Web-site is unreachable please ensure the URL you are trying to analyse is valid and currently live  - e.g. www.rte.ie"

else:
    print ""
    print "Valid web-site URL required to analyse header information - e.g. www.rte.ie"





