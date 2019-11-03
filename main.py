#number = int(input('Введите количество должников: '))
#while number <= 0:
 #   print('Ошибка. Число не может быть меньшим или равным нулю.')
  #  number = int(input('Введите количество должников: '))
#print(number)
#name = str(input('Введите список должников (обратите внимание,
# что список должен заканчиваться пробелом в конце): '))
number = 9
name = """Мясников Никифор Иринеевич Трофимова Альбина Феликсовна """
k = name.count(' ')
print(k)
name_all = ' '
words = 0

for i in range(1,k): #4 words
    n = name.find(' ') #нахожу индекс пробела
    if n == -1:
        name_all = name[:n+1]  # выписываю слово
        name = name[n + 1:]  # отбрасываю слово
        print(name_all, end=' ')
        words += 1
    else:
        name_all = name[:n]  # выписываю слово
        name = name[n + 1:]  # отбрасываю слово
        print(name_all, end=' ')
        words += 1
    if words == 3:
        print()
