import math

print("1. Area of Circle")
print("2. Area of Rectangle")

choice = int(input("Choose: "))

if choice == 1:
    r = float(input("Radius: "))
    area = math.pi * r * r
    print("Area:", area)

elif choice == 2:
    l = float(input("Length: "))
    w = float(input("Width: "))
    print("Area:", l*w)