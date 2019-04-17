class User:
	def __init__(self):
		self.name = input("Type in your name: ")
		print("---------------------")
		print("Hi there,", self.name + "!")
		self.i = 0
		self.actions = [
			"0. Exit",
			"1. Add Expense",
			"2. Get List of Expenses"]
		self.exp_list = []
		
	def show_exp_list(self):
		if len(self.exp_list) == 0:
			print("---------------------")
			print("No expenses yet")
			print("---------------------")
		else:
			print("---------------------")
			print("List of your expenses:")
			for i in self.exp_list:
				print(i.date, "-", i.desc, "-", i.amount)
			print("---------------------")
		
	def add_expense(self):
		self.exp_id = self.i
		self.new_exp = Expense()
		self.new_exp.create(self.exp_id, User)
		self.exp_list.append(self.new_exp)
		self.i += 1
			
class Expense:
	def __init__(self):
		self.id = ""
		self.desc = ""
		self.date = ""
		self.amount = ""
		
	def create(self, id, user):
		self.id = str(id)
		self.desc = input("Enter expense desc: ")
		self.date = input("Enter expense date: ")
		self.amount = "$" + input("Enter expense amount: ")
		print("---------------------")
		print("Expense added:" + "\n ID:", self.id + "\n Desc:", self.desc + "\n Date:", self.date + "\n Amount:", self.amount)
		print("---------------------")
	
	def delete(self, id):
		print("delete")