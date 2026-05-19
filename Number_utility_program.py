#Number utility program
number = int (input ('Enter Number :'))

if number %2 == 1:
	print ('Odd Number')
else :
	print ('Even Number')
	
#positive /negative/zero
if number > 0:
	print ('Positive')
elif number < 0:
	print ('Negative')
else :
	print ('Zero')

#table
print ('\n Multiplication Table :')
for i in range (1,11):
	print (number,'x', i,'=',number*i)
	
#Factorial
fact = 1
for i in range (1,number + 1):
	fact = fact *i
print ('Factorial =', fact)

# reverse number
original = number
reverse =0
while number >0:
	digit = number % 10
	reverse = reverse *10 +digit
	number = number // 10
