numbergames = int(input())
games = str(input())
nranton = games.count("A")
nrdanik = games.count("D")
if nranton > nrdanik:
    print("Anton")
elif nrdanik > nranton:
    print("Danik")
else:
    print("Friendship")
