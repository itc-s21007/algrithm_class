MAX = 5
que = [0]*MAX
head = 0
tail = 0

def enqueue(d):
    global tail
    nt = (tail+1)%MAX

    if nt == head:
        print("これ以上入れません")
    else:
        que[tail] = d
        tail = nt
        print(d, "人入りました")

def dequeue():
    global head
    if head == tail:
        print("取り出すデータが存在しません")
        return None
    else:
        d = que[head]
        head = (head+1)%MAX
        return d

for i in range(1,4):
    enqueue(i)
for i in range(2):
    d = dequeue()
    print(d,"人出ました")
enqueue(1)
print("待ち時間は",(tail - d) * 15,"分です。" )