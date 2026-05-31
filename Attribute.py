class Employee:
	language ='py' #This is an class attribute
	salary = 1200000
	
	#language or salary class hai 
harry = Employee()
harry.name='Harry'  #This is an instance attribute
print (harry.name ,harry.language,harry.salary)


rohan=Employee()
rohan.name ='rohan rathore'
print(rohan.name,rohan.salary,rohan.language)

#Here name is instance attribute and salary and language are attributes as they directly belong to the class..
