basic = int(input("basic: "))
grade = input("grade: ")

if grade=='A':
	allow = 1700
elif grade=='B':
	allow = 1500
elif grade=='C':
	allow = 1300


HRA = (1/5)*basic
DA = (1/2)*basic
PF = (11/100)*basic

gross_salary = basic + HRA + DA + allow - PF

print("the gross salary is: ",gross_salary)



