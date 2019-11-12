def decorate(ff):
    def second(*args, **kwargs):
        print("Called =>", ff.__name__ ,"and Func args =>", args,"Len args =>", len(args),
              "\nType Func first args =>", type(args[0]),"\nType Func second args=>",type(args[1]))
        return ff(*args, **kwargs)
    return second



@decorate
def div(x,y):
    if y == 0:
        return "ділення на 0 неможливе"
    else:
        z = x / y
        return  "ділення можливе і результат", z



z = (div(3,0))

print(z)