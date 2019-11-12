print("Введіть назву файлу =>")
x = input()
try:
    file = open('x')

except IOError as e:
    print(u'файл не вдалось відкрити, його не існує')
    f = open(x)
    print('введіть текс у новий файл з назвою',x)

    f.write(input())

