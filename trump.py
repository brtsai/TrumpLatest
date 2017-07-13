import urllib2
import json
from datetime import datetime
from bs4 import BeautifulSoup

#read the access token in from AccessToken the file
with open("AccessToken") as f:
    access_token = f.readline()
host = "https://graph.facebook.com"
api_version = "v2.9"
id_to_request = "DonaldTrump"
fields_request = "fields=posts.limit(20)&created_time&message&"

my_request = host + "/" + api_version + "/" + id_to_request + "?" + fields_request + "access_token=" + access_token

json_reply = urllib2.urlopen(my_request).read()

parsed_json = json.loads(json_reply)

print "Printing 20 most recent Trump post blurbs:"
for x in range(0,len(parsed_json["posts"]["data"])) :
    print "[" + str(1+x) + " " + parsed_json["posts"]["data"][x]["created_time"] + "]"
    print BeautifulSoup(parsed_json["posts"]["data"][x]["message"], "html.parser").decode("utf-8")







