a = list(map(int, input().split()))
r= []
s = 0
for i in a :
    s += i
    r.append(s)
print(r)