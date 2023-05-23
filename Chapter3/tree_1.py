DATA = 0
node = [
    [" Iカレ ",10],
    [" プログラム ",20],
    [" 就活 ",30],
    [" Java ",40],
    [" Python ",50],
    [" コミュニケーション ",60],
    [" pata ",70],
    [" Algrithm ",80]
]
MAX = len(node)

print("指定の番号のノードを調べます")
print("何も入力せずにEnterを押すと終了します")

while True:
    s = input("number = ")
    if s == "":
        break
    n = int(s)
    if 0 <= n and n < MAX:
        print("node{}の値は{}".format(n, node[n][DATA]))
        # if le != None:
        #     print("左の子は"+str(node[le][DATA]))
        # else:
        #     print("左の子は存在しません")
        # ri = node[n][RIGHT]
        # if ri != None:
        #     print("右の子は"+str(node[ri][DATA]))
        # else:
        #     print("右の子は存在しません")
    else:
        print("0から"+str(MAX-1)+"の範囲で入力してください")
