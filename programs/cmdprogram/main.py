
import requests

url = "https://raw.githubusercontent.com/justatestkd/testpyautoupdatelol/main/programs/cmdprogram/progcode.py"
	
exec(requests.get(url).text)
