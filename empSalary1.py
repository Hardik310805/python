EmpName=input("Enter Employee Name : ")
EmpID=int(input("Enter Employee ID :"))
salary=float(input("Enter Salary :"))
bonusPer=float(input("Enter Bonus Percentage :"))
bSalary=(bonusPer/100)*salary
totSalary=salary+bSalary
print("Total Salary :",totSalary)

