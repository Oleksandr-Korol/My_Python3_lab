height = int(input("Enter height >>> "))
for i in range(height):
    for z in range(height - i):
        print(" ", end="")
    for k in range(i+2):
        print("#", end="")
    for n in range(2):
            print(" ", end="")
    for m in range(i + 2):
            print("#", end="")
    print()

