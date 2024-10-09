first = int(input('Число №1: '))
second = int(input('Число №2: '))
third = int(input('Число №3: '))

if first == second and first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
