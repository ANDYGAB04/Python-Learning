year = int(input())
year += 1
while year != 9013:
    ok = True
    for d in str(year):
        if str(year).count(d) > 1:
            ok = False
    if ok == True:
        break
    year += 1

print(year)
