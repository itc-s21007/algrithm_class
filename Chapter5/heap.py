import random
n = 12
data = [0] * n

for i in range(n):
    data[i] = random.randint(1, 99)
print(data, "もとのでーた")

for i in range((n - 1) // 2, -1, -1):
    p = i
    c = p * 2 + 1
    while c < n:
        if c < n - 1 and data[c] < data[c + 1]:
            c += 1
        if data[p] >= data[c]:
            break
        data[p], data[c] = data[c], data[p]
        p = c
        c = p * 2 + 1
print(data, "初期ヒープ")

d = n - 1
while d > 0:
    data[0], data[d] = data[d], data[0]
    print(f'index0の値：{data[0]} index11の値：{data[d]}を交換')
    p = 0
    c = p * 2 + 1
    while c < d:
        if c < d - 1 and data[c] < data[c + 1]:
            c += 1
        if data[p] >= data[c]:
            break
        data[p], data[c] = data[c], data[p]
        print(f'親の値{data[p]} 子の値{data[c]}')
        p = c
        print(f'index０に子の値が代入された{data[p]}')
        c = p * 2 + 1
    d = d - 1
print(data, "ソート後のデータ")