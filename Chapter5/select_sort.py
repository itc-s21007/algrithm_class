data = ["朝日","高里","子馬","小唄","成果","太田"]
print(data, "もとのデーター")

for i in range(0,len(data)-1):
    m = i
    for j in range(i+1, len(data)):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]
print(data, "ソート後のデータ")
