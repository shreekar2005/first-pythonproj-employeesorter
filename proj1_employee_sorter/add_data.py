def add():
	
	import json
	import show_data
	
	a={}
	
	show_data.show()
	
	with open("employee_sorter_proj1_data.txt") as f0:
		list=json.load(f0)
	
	while True:
		n=input("no. of entries >> ")
		print("\n")
		try:
			n=int(n)
			break
		except:
			print("check your input") 
			
	def write_json(key,val):
		with open("employee_sorter_proj1_data.txt") as f0:
			dict_data=json.load(f0)
			dict_data[key]=val
		with open("employee_sorter_proj1_data.txt","w") as f1:		
			json.dump(dict_data,f1)
				
	for x in range(1,n+1):
		while True:
			id=input("id >> ")
			id_error=0
			for i,c in list.items():
				if i==id:	
					print("this id has already taken!")
					id_error=id_error+1
			if id_error!=1 :
					break
							
		name=input("name >> ")
		salary=input("salary >> ")
		year=input("year(s) worked >> ")
		a[id]={'name':name ,'salary':salary,'year':year}
		print("\n")
		
	for id,category in a.items():
		write_json(id,category)
		print(f"I have added ;\n id of employee => {id} ; name of employee => {category['name']} ; salary of employee => {category['salary']} ; working year(s) => {category['year']}")
	print("\n")
	show_data.show()
	
#add()