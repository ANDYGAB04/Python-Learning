players = str(input())
nrof0 = 0
nrof1 = 0
dangerous = False
for i in range(len(players)):
    if players[i] == "0":
        nrof0 += 1
        nrof1 = 0
    elif players[i] == "1":
        nrof0 = 0
        nrof1 += 1
    if nrof0 == 7 or nrof1 == 7:
        dangerous = True

if dangerous == True:
    print("YES")
else:
    print("NO")
