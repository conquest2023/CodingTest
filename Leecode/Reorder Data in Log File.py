





logs=["dig1 8 1 5 1","let3 art can","dig2 3 6","let2 own kit dig","let3 hrt zero"]
letters, digits = [], []
for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)
print(letters)
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(letters)
print(letters + digits)
