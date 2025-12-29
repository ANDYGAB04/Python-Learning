class SuperList(list):
    def __len__(self):
        return 1000


superlist1 = SuperList([1, 2, 3])
superlist1.append(1)
print(len(superlist1))
