print('Решаем уравнение a*x**2+b*x+c=0')
a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))

discr = b**2 - 4*a*c
print('Дискриминант = ' + str(discr))
if discr < 0:
    print('Корней нет')
elif discr == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print('x1 = ' + str(x1))
    print('x2 = ' + str(x2))


