import json

def check():
	while True:# to checking this programm
		with open("employee_sorter_proj1_data.txt") as f0:
			dict=json.load(f0)
			if not dict:
				print("there is no any employee registered\n\n")
				return False
			else:
				return True
#check()