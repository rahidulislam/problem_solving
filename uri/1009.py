# Salary with bonus
employee_name = input()
salary = float(input())
bonus = (float(input()) * 15) / 100
total = salary + bonus
print(f"TOTAL = R$ {total:.2f}")
