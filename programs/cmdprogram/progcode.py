import math

while True:
	cmd = input("Enter command here: ")
	if cmd:
		if cmd == "/exec" or cmd == "/execute":
			code = input("Enter code for execute here: ")
			if code:
				exec(code)
		if cmd == "/calc" or cmd == "/calculate" or cmd == "calculator":
			opp = input("Choose a opperate(+ or -): ")
			numbone = input("Number one: ")
			numbtwo = input("Number two: ")
			if opp:
				if opp == "-":
					if int(numbone) >= 0:
						if int(numbtwo) >= 0:
							result = int(numbone)-int(numbtwo)
							print("Result: "+str(result))
				if opp == "+":
					if int(numbone) >= 0:
						if int(numbtwo) >= 0:
							result = int(numbone)+int(numbtwo)
							print("Result: "+str(result))
