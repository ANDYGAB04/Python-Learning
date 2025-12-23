def swap_letter(s, index, new_char):
    return s[:index] + new_char + s[index + 1 :]


n, t = map(int, input().split())
s = input()

while t != 0:
    i = 0
    while i < n - 1:
        if s[i] == "B" and s[i + 1] == "G":
            s = swap_letter(s, i, "G")
            s = swap_letter(s, i + 1, "B")
            i = i + 2
        else:
            i = i + 1
    t -= 1

print(s)
