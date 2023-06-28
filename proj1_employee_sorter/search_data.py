import json
import show_data
import check_data

def s1earch(category,specification):
	number=0
	with open("employee_sorter_proj1_data.txt") as f0:
		list=json.load(f0)	
	for key,val in list.items():
		if category=='id':
			if key==specification:
				print('id of employee =>',key,'  name of employee =>',val['name'],'  year(s) worked =>',val['year'],'  salary of employ =>',val['salary'])
				number=number+1		
		elif val[category]==specification:
			print('id of employee =>',key,'  name of employee =>',val['name'],'  year(s) worked =>',val['year'],'  salary of employ =>',val['salary'])
			number=number+1
	print(f"there is/are {number} employee(s) with given {category}")
	print("\n")

def search():
	
	if not check_data.check():
		return # terminates function
	
	show_data.show()
		
	try:
		category=input('by which category do you want to get info of Employee ? (id/salary/name/year) >> ')
		specification=input(f"entre {category} >> ")
		s1earch(category,specification)
	except:
		print("check your input \n")

#search()