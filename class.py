class Employee:

    pass

emp_1 = Employee()

emp_2 = Employee()


print(emp_1)
print(emp_2)


emp_1.first = "Subash"
emp_1.last = "KC"
emp_1.email = "msubash_213@yahoo.com"
emp_1.pay = 40000


emp_2.first = "Ambika"
emp_2.last = "KC"
emp_2.email = "msubash213@gmail.com"
emp_2.pay = 50000

print(emp_1.email)
print(emp_2.email)
