import show_data # to search info of employee
import add_data # to add data of new employee
import update_data # to update data of registered employee
import delete_data # to delete info of registered employee
import search_data # to search data of registered employee

#show_data.show() # to see data
#add_data.add() # to add data
#update_data.update() # to update data
#delete_data.delete() # to delete data
#search_data.search() # to search data

def task(command):
#	print("\n")
	exec(f"{command}_data.{command}()")

while True:
	command=input("what do you want to do with data ? (show/add/update/delete/search) >> ")
	try:
		task(command)
	except:
		print("check your input\n")
	



