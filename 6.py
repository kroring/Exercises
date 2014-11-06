import re, urllib, urllib2, sys, httplib
from urlparse import urljoin

# Initialize global variables
news_site_url = ""
headline_string = ""

def retrieveHeadlineMatches():

        # Local variables
        href_item = ""
        headline_urls = ""
        result_counter = 1
        
        # Try to retrieve URL content
        try:

                url_content = urllib.urlopen(news_site_url).read()
                       
        # If something goes wrong e.g. web-site is unreachable, catch and provide user friendly feedback
        except urllib2.HTTPError, e:
                print ""
                sys.exit("This URL you entered (" + news_site_url[7:] + ") is unreachable. Please ensure the URL you are trying to analyse is valid and currently live. Example of valid URL: www.skynews.com")
        except urllib2.URLError, e:
                print ""
                sys.exit("This URL you entered (" + news_site_url[7:] + ") is unreachable. Please ensure the URL you are trying to analyse is valid and currently live. Example of valid URL: www.skynews.com")
        except httplib.HTTPException, e:
                print ""
                sys.exit("This URL you entered (" + news_site_url[7:] + ") is unreachable. Please ensure the URL you are trying to analyse is valid and currently live. Example of valid URL: www.skynews.com")
        except Exception:
                print ""
                sys.exit("This URL you entered (" + news_site_url[7:] + ") is unreachable. Please ensure the URL you are trying to analyse is valid and currently live. Example of valid URL: www.skynews.com")

        print ""
        print "Headline Matches: "
        print ""

        # Loop through HTML content that gets split into URL items (purposely excluding left closing anchor tag angle bracket out for later filtering)
        for href_item in url_content.split("/a>"):

                # If headline topic string is in current URL item proceed further with processing, otherwise move onto next URL item
                if headline_string in href_item:

                        # Retreive all href tag values within URL item and add to list headline_url (can be two for same headline - one for image link and
                        # other for text link.. each linking to the same URL)
                        headline_urls= re.findall(r'href=[\'"]?([^\'" >]+)', href_item)

                        # Print out full headline match (prefixing with index value). The regex will take everything between first angle bracket
                        # before and after full headline topic string match e.g. <span> Malaysia Airlines </span> -> Malaysia Airlines
                        print str(result_counter) + ') ' + re.search(r".*>((?:(.*?)(?:" + headline_string + ")(.*?)).*)<", href_item).groups()[0]

                        # Print out the full URL belonging to the headline topic match (if only a partial headline e.g. /headlines/Ukraine, the
                        # site URL will be appended). As well, only last href in headline_url list taken to remove duplicates caused by image links
                        print urljoin(news_site_url, max(headline_urls))

                        print ''

                        # Increment headline counter by 1
                        result_counter += 1
                        
        # If there are no headlines returned - print None
        if result_counter < 2:
                print "None"

# If block to determine action. If no parameters passed: prompt user for a news web-site URL and then a news topic.
# If 1 or more parameters are passed, execute the else block
if len(sys.argv) == 1:
        
        while news_site_url.strip() == "":
                news_site_url = raw_input("Please enter a news web-site URL (e.g. www.skynews.com) to analyse: ")
                
        news_site_url = "http://" + news_site_url
        
        while headline_string.strip() == "":
                headline_string = raw_input("Please enter a topic to news topic search for (e.g. Malaysia): ")
                
        retrieveHeadlineMatches()
        
else:
        # Outer if to ensure no more or less than two parameters are given - a news web-site URL and a headline topic string
        if len(sys.argv) <= 3:

                if len(sys.argv) >= 3:

                        news_site_url = "http://" + sys.argv[1]
                        headline_string = sys.argv[2]
                        retrieveHeadlineMatches()
                        
                else:
                        print ''
                        print 'Two parameters required: a news web-site URL and headline topic to search for. e.g. python 6.py www.skynews.com Malaysia'
                        
        else:
                print ''
                print 'No more than two parameters accepted: a news web-site URL and news topic to search for. e.g. python 6.py www.skynews.com Malaysia'


            
