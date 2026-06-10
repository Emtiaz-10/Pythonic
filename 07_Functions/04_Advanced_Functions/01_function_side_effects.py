def ad(lst):
    lst.append(9)

ar = [43,5]
ad(ar)
print(ar)

def ad2(lst):
    return lst + [0]

n = ad2(ar)


print(ar,n)