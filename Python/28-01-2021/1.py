def fread(fname):
    with open(fname) as f:
        c = f.readlines()
    print(c)
    print(len(c))


fread("demo")
