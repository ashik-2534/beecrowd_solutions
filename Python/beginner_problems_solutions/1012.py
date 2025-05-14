input_data = input().split()
A, B, C = input_data
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
area_of_triangle = A * C * 0.5
area_of_circle = pi * C**2
area_of_trapezium = (A+B)*C/2
area_of_square = B**2
area_of_rectangle = A*B
print(f"TRIANGULO: {area_of_triangle:.3f}")
print(f"CIRCULO: {area_of_circle:.3f}")
print(f"TRAPEZIO: {area_of_trapezium:.3f}")
print(f"QUADRADO: {area_of_square:.3f}")
print(f"RETANGULO: {area_of_rectangle:.3f}")