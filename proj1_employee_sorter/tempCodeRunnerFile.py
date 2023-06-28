
	exec(f"{command}_data.{command}()")

while True:
	command=input("what do you want to do with data ? (show/add/update/delete/search) >> ")
	try:
		task(command)
	except:
		print("check your input\n")
	



