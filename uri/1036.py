"""Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the
roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
"""
a, b, c = list(map(float, input().split()))
formula = b ** 2 - (4 * a * c)
if a == 0 or formula < 0:
    print("Impossivel calcular")
else:
    r1 = (-b + formula ** 0.5) / (2 * a)
    r2 = (-b - formula ** 0.5) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
