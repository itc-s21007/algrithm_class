a = [1,3,4,7,8,9]
b = [0,2,5,6]
na = len(a)
nb = len(b)
c = [0]*(na + nb)
i = 0
j = 0
p = 0

print(a, "データA")
print(b, "データB")

while i < na and j < nb:
    if a[i] <= b[j]:
        c[p] = a[i]
        i += 1
        p += 1
        print(c,"i")
    else:
        c[p] = b[j]
        j += 1
        p += 1
        print(c,"j")
print(c, "マージ途中のデータ")

while i < na:
    c[p] = a[i]
    i += 1
    p += 1

while j < nb:
    c[p] = b[j]
    j += 1
    p += 1

print(c, "マージ後のデータ")
