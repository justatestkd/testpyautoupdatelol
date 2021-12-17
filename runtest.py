import requests

url = "https://raw.githubusercontent.com/justatestkd/testpyautoupdatelol/main/main.py"

def UpdateFile():
	file = open("test.py",'w')
	page = requests.get(url)
	file.write(page.text)
	file.close()
	return "Success"
	
print("Update file answ: "+UpdateFile())
print("Trying to run the code...")
from test import Main
print(Main.RunCode())
