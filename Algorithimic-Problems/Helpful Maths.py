s = input().strip()
li = []
for i in s:
    if i != "+":
        d = int(i)
        li.append(d)

li.sort()
news = ""
for i in li:
    news = news + str(i) + "+"
print(news[0 : len(news) - 1])
