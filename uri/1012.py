a, b, c = list(map(float, input().split()))
triangle = 0.5 * a * c
circle = 3.14159 * c ** 2
trapezium = 0.5 * (a + b) * c
squire = b ** 2
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {squire:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
