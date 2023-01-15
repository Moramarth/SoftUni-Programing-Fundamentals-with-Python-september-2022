from math import sqrt, floor

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

vector_1 = sqrt(x_1**2 + y_1**2)
vector_2 = sqrt(x_2**2 + y_2**2)

if vector_1 < vector_2:
    print(f"({floor(x_1)}, {floor(y_1)})")
elif vector_2 < vector_1:
    print(f"({floor(x_2)}, {floor(y_2)})")
else:
    print(f"({floor(x_1)}, {floor(y_1)})")
