import json
import show_data
import check_data

def delete_json(key):
	with open("employee_sorter_proj1_data.txt") as f3:
		dict_data=json.load(f3)
		dict_data.pop(key)
	with open("employee_sorter_proj1_data.txt","w") as f1:		
		json.dump(dict_data,f1)


def delete():
			
	a={}
	
	if not check_data.check():
		return # terminates function
		
	show_data.show()
	
	with open("employee_sorter_proj1_data.txt") as f0:
		list=json.load(f0)	
	
	while True:
		n=input("no. of employees that you have to delete their info >> ")
		print("\n")
		try:
			n=int(n)
			break
		except:
			print("check your input\n") 
				
	for x in range(1,n+1):
		while True :
			while True:
				id_del=input("id >> ")
				id_error=0
				for i,c in list.items():
					if i==id_del:	
						id_error=id_error+1
						
				if id_error==1 :
					break
				else:
					print("there is no employee with given id")
					
			for id,category in list.items():
				if id==id_del:
					print(f"id of employee => {id} ; name of employee => {category['name']} ; salary of employee => {category['salary']} ; working year(s) => {category['year']}")		
											
			confirmation=input("may I delete info on this ID ? (y/n) >> ")
			if confirmation=='y':
				print("\n")
				break
			else:
				print("ok, I am not deleting! please rentre ID \n ")
				
		delete_json(id_del)
		print(f"I have deleted ;\n id of employee => {id} ")
		print("\n")
		if not check_data.check():
			return # terminates function
		show_data.show()	
	
#delete()