animals = {'a':'aardvark', 'b':'baboon', 'c':'coati'}
animals.update({'d':'hiena'})

for num , item in enumerate (animals):
    num1 = num + 1
    print(num1,":", item,":", animals[item])


print(animals)
print(">>>",len(animals),"кількість елементів у словнику")

while True:
    print("Для виходу використайте '0'")
    key_a = input("введіть значення ключа для пошуку")
    if key_a == "0":
        break
    elif animals.get(key_a):
        print("Так ваш ключ існує і його значння ", animals[key_a])

    else:
        print("ключа немає")