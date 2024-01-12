baby_words = set()
n = int(input("Enter number for lines: "))
for i in range(n):
    words = input("Enter baby words: ").split(" ")
    baby_words.update(words)
print(*baby_words, sep="\n")
