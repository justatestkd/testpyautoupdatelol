import requests

def getcodefromraw(link):
	return requests.get(link).text
