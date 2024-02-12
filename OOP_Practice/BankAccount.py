class BankAccount:
	
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance
		
	def deposit(self, amount):
		self.balance = self.balance + amount
		return 'Deposit Accepted!'
	
	def withdraw(self, amount):
		if self.balance - amount < 0:
			return f"Don't have sufficient funds, short on $ {amount - self.balance}"
		self.balance = self.balance - amount
		return f'Withdrawn $ {amount}, remaining balance is {self.balance}'
	
	def __str__(self):
		return f'Account owner is {self.owner}\nAccount balance is ${self.balance}'
	

acct1 = BankAccount('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.withdraw(50))
print(acct1.balance)
acct1.deposit(222)
print(acct1.balance)
print(acct1.withdraw(500))
