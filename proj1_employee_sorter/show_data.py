def show():
	
	import json

	with open("employee_sorter_proj1_data.txt") as f0:
		dict=json.load(f0)
		#print(dict,"\n")
	
	def sort_in_well_manner(dict):
		list_vals=[]
		for key,val in dict.items():
			for key1,val1 in val.items():
				list_vals.append(val1)
		
		try:		
			maxlen=(len(max(list_vals,key=len)))
	
			for id,category in dict.items():				
				print("id of employee => "+id+" "*(maxlen-len(id)), "; name of employee => "+category['name']+" "*(maxlen-len(category['name'])), "; salary of employee => "+category['salary']+" "*(maxlen-len(category['salary'])), "; working year(s) => "+category['year'])
			print("\n")
		except:
			print("there is no any employee registered\n")
							
	sort_in_well_manner(dict)
	
#show()