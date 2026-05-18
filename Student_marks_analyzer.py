#student_marks_analyzer
name = [ ]
marks = [ ]
name = input ('Enter your name :')
English = int (input('English :'))
Hindi = int (input ('Hindi:'))
Maths = int (input ('Maths:'))
Chemistry = int (input ('Chemistry:'))
Physics = int (input ('Physics :'))
 
#percentage
total = English + Hindi + Maths + Chemistry + Physics
percentage = (total / 500 ) * 100

print ('total marks : ', total )
print ('percentage :',percentage,'%')
#Grade
if percentage >= 90:
	print ('Grade : A')
	print ('PASS in first division')
elif percentage >= 75:
	print ('Grade : B')
	print ('PASS')
elif percentage >= 50:
	print ('Grade : C')
else :
	print ('Fail')
	


