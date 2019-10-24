import os

def check(ll):

    bord_True = []

    for i in range(1, 16):
        bord_True.append(i)
    bord_True.append(0)
    if bord_True == ll:
        print("Вітаю! Ви переможець гри 15-шки")
        bord_chek = True
    else:
        bord_chek = False

    return bord_chek




def print_bord(ll):
    #os.system("clear") # for windows you need to use "cls" instead of "clear"
    for i in range(16):
        if (i == 4):
            print("")
        if (i == 8):
            print("")
        if (i == 12):
            print("")
        if ll[i] == 0:
            print("__", end="\t")
        else:
            print(ll[i],end="\t")
    print()

def check_move(move, bb):

    location = bb.index(move)
    if (location - 4 >= 0) and (bb[location - 4] == 0):
        bb_1 = bb[location]
        bb[location] = bb[location - 4]
        bb[location - 4] = bb_1
    if (location - 1 >= 0) and (bb[location - 1] == 0):
        bb_1 = bb[location]
        bb[location] = bb[location - 1]
        bb[location - 1] = bb_1
    if (location + 4 <= 15) and (bb[location + 4] == 0):
        bb_1 = bb[location]
        bb[location] = bb[location + 4]
        bb[location + 4] = bb_1
    if (location + 1 <= 15) and (bb[location + 1] == 0):
        bb_1 = bb[location]
        bb[location] = bb[location + 1]
        bb[location + 1] = bb_1


    return True



if __name__ == "__main__":
    print("Ви граєте у гру 15-шки")
    bord = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0]
    while not check(bord):
        print_bord(bord)
        while True:
            your_try = int(input("Введіть число  1-15 >> "))
            if check_move(your_try, bord):
                break