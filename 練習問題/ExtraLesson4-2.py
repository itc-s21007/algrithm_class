import random
import bisect
n = 0
right = 100
left = 1
r = random.randint(1, 100)
s = int(input("１〜１００までの値を入力してください"))

s = bisect.bisect(r,s)
