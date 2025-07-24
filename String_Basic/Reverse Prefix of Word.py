word = "abcdefd"
ch = "b"

pos = word.index(ch)+1
print(word[:pos][::-1]+word[pos:])
