import requests

def getcodefromraw(link):
	return requests.get(link).text

def getgitcode(gitpath,filepath):
	link = "https://raw.githubusercontent.com/"+gitpath+"/main/"+filepath
	return requests.get(link).text
