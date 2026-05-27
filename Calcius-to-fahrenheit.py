#calcius to fahrenheit
def f_to_c(f):
	return 5*(f-32)/9
	
f= int (input('ENTER TEMPERATURE IN F :'))
c = f_to_c(f)
print(f'{round(c,2)}°C')

f= int (input('ENTER TEMPERATURE IN F :'))
c = 5*(f-32)/9
print (c,'°C')
