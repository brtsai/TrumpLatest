import urllib2
import json

#read the access token in from AccessToken the file
with open("AccessToken") as f:
    access_token = f.readline()
host = "https://graph.facebook.com"
api_version = "v2.9"
id_to_request = "DonaldTrump/"
fields_to_request = ""
fields_request = "fields=posts.limit(5)" + fields_to_request + "&"

my_request = host + "/" + api_version + "/" + id_to_request + "?" + fields_request + "access_token=" + access_token

print "Printing request_url"
print my_request

json_reply = urllib2.urlopen(my_request).read()

parsed_json = json.loads(json_reply)

print "Printing json_reply:"
print json_reply
print

print "Printing prettified parsed json:"
print json.dumps(parsed_json, indent=4, sort_keys=True)
print

#print "Printing parsed_json[\"name\"]:"
#print parsed_json["name"]
print "Printing posts:"
print parsed_json["posts"]
print

print "Printing prettified posts:"
print json.dumps(parsed_json["posts"], indent=4, sort_keys=True)
print

print "Printing 5 most recent posts:"
for x in range(0,len(parsed_json["posts"]["data"])) :
    print json.dumps(parsed_json["posts"]["data"][x]["message"], indent=4, sort_keys=True)







