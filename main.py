# Программа для нахождения корней квадратных уравнений

print('Решаем квадратное уравнение ax²+bx+c=0')
# Проверка входных данных
a = input('Коэффициент a: ')
while type(a) != float:
    try:
        float(a)
        break
    except ValueError:
        print('Введенное значение не является числом')
        a = input('Коэффициент a: ')
a = float(a)

b = input('Коэффициент b: ')
while type(b) != float:
    try:
        float(b)
        break
    except ValueError:
        print('Введенное значение не является числом')
        b = input('Коэффициент b: ')
b = float(b)

c = input('Коэффициент c: ')
while type(c) != float:
    try:
        float(c)
        break
    except ValueError:
        print('Введенное значение не является числом')
        c = input('Коэффициент c: ')
c = float(c)

# Нахождение дискриминанта квадратного уравнения
D = b**2 - 4*a*c
# Вывод корней квадратного уравнения
if a == 0:
    x = -c / b
    print(f'Уравнение не является квадратным! \nx={x}')
elif D < 0:
    print('Корней нет')
elif D == 0:
    x = -b / (2 * a)
    print(f'x ={x}')
else:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print(f'Корни уравнения: \nx1 = {x1}, x2 = {x2}')
