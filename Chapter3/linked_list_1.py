MAX = 5
data = [None]*MAX
pointer = [None]*MAX
head = 0

def add_list(d):
    n = -1
    for i in range(MAX):
        if data[i] == None:
            n = i
            break
    if n == -1:
        print("データ領域に空きがありません")
        return False
    for i in range(MAX):
        if data[i] != None and pointer[i] == None:
            pointer[i] = n
            break
    data[n] = d
    pointer[n] = None
    return True

def del_list(d):
    global head
    n = -1
    for i in range(MAX):
        if data[i] == d:
            n = i
            break
    if n == -1:
        print("そのデータは存在しません")
        return False
    if n != head:
        for i in range(MAX):
            if pointer[i] == n:
                pointer[i] = pointer[n]
    else:
        head = pointer[n]
        if head == None:
            head = 0
    data[n] = None
    pointer[n] = None
    print(d, "を削除しました")
    return True

def put_list():
    p = head
    while True:
        print(data[p], end="->")
        if pointer[p] == None:
            print("EOF")
            break
        p = pointer[p]


s = ["東京","大阪", "福岡", "京都"]
add_list(s)
put_list()
i = s.pop(1)
a = s.pop(1)
s.insert(1,a)
s.insert(2,i)
put_list()
