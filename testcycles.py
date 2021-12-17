import requests

def runtesttwo():
	 code = requests.get("https://raw.githubusercontent.com/justatestkd/testpyautoupdatelol/main/runtesttwo.py")
	 return code.text
	 
while True:
	 print("Cycles test!")
	 print("Press 1 to execute the code.")
	 press = input()
	 if press:
	 	if press == "1":
	 		exec(runtesttwo())
	 		print("\n")
