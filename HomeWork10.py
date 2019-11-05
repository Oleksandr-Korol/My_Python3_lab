cliper_dict = {}
name = ['Vova', 'Valja', 'Petro', 'Ivan']
year = [1990, 2000, 1995, 2002]

for key, val in zip(name, year,):
    cliper_dict[key] = val
print(cliper_dict)

print(sorted(cliper_dict))
print(sorted(cliper_dict.values()))

for i in sorted(name):
    print(i, cliper_dict[i])
print("--------------------")

for num in sorted(cliper_dict.values()):
    for i in cliper_dict:
        if cliper_dict[i] == num:
            print(i, cliper_dict[i])
