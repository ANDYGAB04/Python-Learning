word = str(input())
word = word.lower()
if "a" in word:
    word = word.replace("a", "")
if "u" in word:
    word = word.replace("u", "")
if "i" in word:
    word = word.replace("i", "")
if "o" in word:
    word = word.replace("o", "")
if "e" in word:
    word = word.replace("e", "")
if "y" in word:
    word = word.replace("y", "")

for i in range(len(word)):
    print("." + word[i], end="")
