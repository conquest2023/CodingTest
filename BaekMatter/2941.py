result = 0
for i in range(int(input())):
    word = input()
    list(word) == sorted(word, key=word.find)
    print(word)
    result += 1
print(result)