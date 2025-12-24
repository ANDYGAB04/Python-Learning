word = str(input())
ok1 = word[:].isupper()
ok2 = word[1:].isupper()
ok3 = False
if len(word) == 1:
    ok3 = word[:].islower()
if ok2:
    word = word[0].upper() + word[1:].lower()
if ok1:
    word = word[:].lower()
if ok3:
    word = word[0].upper()
print(word)
