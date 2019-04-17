from new import User


Gordo = User()

while True:
	print("---------------------")
	for o in Gordo.actions:
		print(o)
	print("---------------------")
	try:
		action_to_perform = int(input("Select an action: "))
		if action_to_perform < 0:
			print("Enter a valid option")
		elif action_to_perform > len(Gordo.actions):
			print("Enter a valid option")
		elif action_to_perform == 0:
			break
		elif action_to_perform == 1:
			Gordo.add_expense()
		elif action_to_perform == 2:
			Gordo.show_exp_list()
	except(ValueError):
		print("Enter a valid option")