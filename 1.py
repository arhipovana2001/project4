print('--------------------------------------------------------------------------')
print('        ФИ         |     долг     |     платеж     |    остаток долга    |')
print('                   |   тыс. руб.  |    тыс. руб.   |      тыс. руб.      |')
print('--------------------------------------------------------------------------')

registry = '''Мясников Никифор 57689/Трофимова Альбина 342525/Макаров Артем 444/Ревтова Лидия 3893/Зайцева Анастасия 829/'''

k = 0
debt = 0
name = ''
balance_owed = 0
first_column = 19
payment = 0

number = registry.count('/')
for i in range (1, number + 1):
    index = registry.find('/')
    name = registry[:index]
    registry = registry[index + 1:]
    k = name.count(' ')
    name_all = ''
    while k + 1 > 0:
        name = name
        n1 = name[:name.find(' ') + 1]
        #if n1.isdigit():
         #   debt = int(n1)
        name_all = name_all + n1
        name = name[name.find(' ') + 1:]
        k -= 1
    symbol = first_column - len(name_all)
    print(name_all + ' ' * symbol, end = '')
    print('|', end = '')
    payment = str(ord(name_all[0]))
    debt = payment[::-1]
    payment = int(payment)
    debt = int(debt)
    print(format(debt, "14.0f"), end='')
    print('|', end='')
    print(format(payment, "16.0f"), end='')
    print('|', end='')
    balance_owed = debt - payment
    print(format(balance_owed, "21.0f"), end='')
    print('|')


    #debt = int(input('Введите долг: '))
    #while debt < 0:
     #   print('Ошибка. Число не может быть меньше нуля.')
      #  debt = int(input('Введите долг: '))

    #payment = int(input('Введите платеж: '))
    #while payment < 0:
     #   print('Ошибка. Число не может быть меньше нуля.')
      #  payment = int(input('Введите платеж: '))

    #balance_owed = debt - payment
    #print('Остаток долга =', balance_owed)
print('--------------------------------------------------------------------------')