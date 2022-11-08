
mlist = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

for i in range(10):
    for a in mlist:
        if type(a) == list:
            c = []
            k = len(a)
            for b in range(k):
                c.append(a[b])
            b = mlist.index(a)
            h = 0
            mlist.remove(a)
            while k > 0:
                mlist.insert(b, c[h])
                b += 1
                k -= 1
                h += 1

#input = ('''[[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]''')
#output = ('''[1, 'a', 'cat', 2, 3, 'dog', 4, 5]''')
print(mlist)

##########################################3
zz = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
y = []


def duzleme(z):
    for i in z:
        if type(i) == list:
            duzleme(i)
        else:
            y.append(i)
    return y


print(duzleme(zz))
