def quadratic_solution(a, b, c, x):
  return a*x**2+b*x+c
with open('input.txt', 'r') as file:
    lines = file.readlines()
    a, b, c, x = map(float, lines[0].split()) 
print("temperature for hardcoded coefficients at time")
print(quadratic_solution(a, b, c, x))