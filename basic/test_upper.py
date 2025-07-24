input_str = "hi how are you"
l =[]
def upperstr(str):
    for i in str.split():
        l.append(i[0].upper() + i[1:])
    #print(l)
    str1 = " ".join(l)
    print(str1)

upperstr(input_str)
