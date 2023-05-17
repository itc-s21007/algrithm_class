MAX = 5
stack = [0]*MAX
sp = 0

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
        print("本", d, "を追加")
    else:
        print("これ以上データを入れられません")

def pop():
    global sp
    if sp > 0:
        sp = sp - 1
        return stack[sp]
    else:
        print("取り出す本が存在しません")
        return None

for i in range(2):
    push(i)
d = pop()
print("取り出した本", d)
for i in range(3):
    push(i)