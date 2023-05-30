LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, 10],
    [3, 4, 20],
    [5, None, 30],
    [None, None, 40],
    [6, 7, 50],
    [None, None, 60],
    [None, None, 70],
    [None, None, 80]
]
MAX = len(node)

print("指定の番号のノードを調べます")
print("何も入力せずにEnterを押すと終了します")

n = 0

if n <= MAX:
    print(node[n][DATA])
    le = node[n][LEFT]
    if le != None:
        print(node[le][DATA])
    else:
        print("None")
    
