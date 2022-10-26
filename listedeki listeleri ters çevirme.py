mylist = [[1, 2], [[3, 4], [5, 6, 7]]]
for char in mylist:
    if type(char) == list:
        for i in char:
            if type(i) == list:
                mylist[mylist.index(char)][char.index(i)] = i[::-1]
        mylist[mylist.index(char)] = char[::-1]
mylist = mylist[::-1]
#input = [[1, 2], [[3, 4], [5, 6, 7]]]
#output = [[[[7, 6, 5], [4, 3]], [2, 1]]
print(mylist)
