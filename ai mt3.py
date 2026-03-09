from sympy import symbols, solve

x = symbols('x')

equation = input("Enter equation (example: x+5-10): ")

result = solve(equation)

print("Solution:", result)