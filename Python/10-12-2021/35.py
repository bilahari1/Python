str1 = input("Enter a string ")


def fun(str):
    if str[-3:] == 'ing':
        print(str + "ly")
    else:
        print(str + "ing")


fun(str1)
