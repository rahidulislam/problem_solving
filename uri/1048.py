# Salary Increase

salary = float(input())
if salary <= 400.00:
    percentage = 15
elif 400.01 <= salary <= 800.00:
    percentage = 12

elif 800.01 <= salary <= 1200.00:
    percentage = 10
elif 1200.01 <= salary <= 2000.00:
    percentage = 7
else:
    percentage = 4
earning = (salary * percentage) / 100
new_salary = salary + earning

print(f'''Novo salario: {new_salary:.2f}
Reajuste ganho: {earning:.2f}
Em percentual: {percentage} %''')
