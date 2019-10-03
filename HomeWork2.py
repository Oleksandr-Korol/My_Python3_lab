
print("Рівняння має вигляд >>> a*x^2+b*x+c=0")
numberA = input("введіть занчення a >>> ")
numberA = int(numberA)
numberB = input("введіть занчення B >>> ")
numberB = int(numberB)
numberC = input("введіть занчення C >>> ")
numberC = int(numberC)
numberD = numberB * numberB - 4 * numberA * numberC
print(numberD)
if numberD > 0:
    x1 = (-numberB + numberD ** 0.5) / 2 * numberA
    x1 = float(x1)
    print("Корінь рівння x1")
    print(x1)
    x2 = (-numberB - numberD ** 0.5) / 2 * numberA
    x2 = float(x2)
    print("Корінь рівння x2")
    print(x2)

elif numberD == 0:
    x3 = (-numberB) / 2 * numberA
    print("Корінь рівння x1=x2")
    print(x3)

else:
    numberD < 0
    print("Рівняння коренів немає")