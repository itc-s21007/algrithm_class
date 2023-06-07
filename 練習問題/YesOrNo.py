LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, "38.5℃以上のねつがある？"],
    [3, 4, "胸がヒリヒリする"],
    [5, 6, "元気がある？"],
    [None, None, "速攻病院"],
    [None, None, "解熱剤で病院"],
    [None, None, "様子を見る"],
    [None, None, "氷枕で病院"]
]
MAX = len(node)
a = 0

while True:
    print(node[a][DATA], end="")
    s = input("(y/n)")
    if s == "":
        break
    if s == "y":
        a = node[a][LEFT]
    if s == "n":
        a = node[a][RIGHT]
    if node[a][LEFT] == None and node[a][RIGHT] == None:
        print("診断結果：",node[a][DATA])
        break





