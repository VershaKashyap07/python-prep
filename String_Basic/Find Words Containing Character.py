words = ["leet","code"]
x = "e"
Output= []

for i in range(len(words)):
    if words[i].index(x)!=-1:
        Output.append(i)

print(Output)

