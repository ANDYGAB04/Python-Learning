number = input().strip()
chars = list(number)
for i, ch in enumerate(chars):
    d = int(ch)
    if i == 0 and d == 9:
        continue
    if 9 - d < d:
        chars[i] = str(9 - d)

print(''.join(chars))
