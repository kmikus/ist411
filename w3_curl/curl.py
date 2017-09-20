# Project: urllib, json and python lab
# Purpose Details: To read data from a url and output into json file
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 9/7/17
# Last Date Changed: 9/7/17
# Rev: 0.1

import sys, urllib.parse, urllib.request, json
 
try:
	# parse url for encoding
	url = "https://jsonplaceholder.typicode.com/posts/1/comments"
	clean_url = urllib.parse.urlparse(url)

	# request body from url
	response = urllib.request.urlopen(clean_url.geturl())
	payload = response.read()
	encoding = response.info().get_content_charset("utf-8")

	# convert to json format
	jsonStream = json.loads(payload.decode(encoding))
	jsonDump = json.dumps(jsonStream, indent=4)
	with open("curl.json", "w") as outFile:
		outFile.write(jsonDump)
	print(jsonDump)
except:
	e = sys.exc_info()[0]
	print("error: {}".format(e))

