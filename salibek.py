import math

a, b, c = float(input()), float(input()), float(input())

d = b**2 - 4*a*c

if d < 0:
  print("Нет решений!")
elif a == 0 and b == 0 and c == 0:
  print("Деление на 0")
elif d == 0:
  print(-b/(2*a))
else:
    print(((-b + math.sqrt(d))/(2*a)), " ", ((-b - math.sqrt(d))/(2*a)))