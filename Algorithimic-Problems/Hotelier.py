n = int(input().strip())
events = input().strip()
hotel = list("0000000000")

for ch in events:
    if ch == "L":
        for i in range(10):
            if hotel[i] == "0":
                hotel[i] = "1"
                break
    elif ch == "R":
        for i in range(9, -1, -1):
            if hotel[i] == "0":
                hotel[i] = "1"
                break
    else:
        hotel[int(ch)] = "0"

print("".join(hotel))
