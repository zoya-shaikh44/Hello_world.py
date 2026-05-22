#factorial
n = int (input ('Enter the number :'))
n1 = int (input('Enter the number1 :'))
n2 = int (input('Enter the number2 :'))
n3 = int (input('Enter the number3 :'))
n4 = int (input('Enter the number4 :'))
product = 1
for i  in range (1,n+1):
	product = product * i
print (f'the factorial of {n} is {product}')

for i in range (1,n1+1):
	product = product+i
print (f'the factorial of {n1} is {product}')

for i in range (1,n+1):
	product = product*1
print (f'the factorial of {n2} is {product}')

for i in range (1,n+1):
	product =product*1
print (f'the factorial of {n3} is {product}')

for i in range (1,n+1):
	product = product*1
print (f'the factorial of {n4} is {product}')


