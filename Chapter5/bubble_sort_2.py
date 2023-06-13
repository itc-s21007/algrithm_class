data = [9, 4, 7, 2, 3, 8, 6, 1, 5,0]
n = len(data)
print(data, "もとのデータ")

for i in range(0, n - 1):
    for j in range(0, n-1-i):
        if data[j] > data[j + 1]:
            data[j], data[j+1] = data[j+1], data[j]

print(f"\033[38;2;255;0;255m{data}\033[0m", end=" ")
