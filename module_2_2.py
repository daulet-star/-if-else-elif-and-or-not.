first=int(input('введите три числа-'))
second=int(input('введите три числа-'))
third=int(input('ведите три числа-'))

if first == second or first == third or second == third:
    print('2 ')
elif first==second==third:
    print('3 ')
else:
    print(' 0')