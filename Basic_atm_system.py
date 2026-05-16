#ATM_simultion
balance = int (input ('Enter your balance : '))
deposit = int (input ('Enter your deposit amount : '))
withdraw = int (input ('Enter your withdrawing amount : '))

def addition (balance ,deposit):
	total_balance = balance + deposit
	print ('Total balance after deposit :', total_balance )
	
def subtraction (balance ,withdraw):
	total_balance = balance-withdraw
	print ('Total balance after withdrawal :', total_balance)
	
addition (balance ,deposit)
subtraction (balance ,withdraw)
