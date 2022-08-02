a = [int(a) if a.isdigit() else float(a) for a in input().split(' ')[1:]]
b = [int(a) if a.isdigit() else float(a) for a in input().split(' ')[1:]]
total = (a[0] * a[1]) + (b[0] * b[1])
print(f"VALOR A PAGAR: R$ {total:.2f}")
