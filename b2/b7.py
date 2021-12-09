n = int(input())
d= []
dt = [] 
for i in range(n):
    a, b = input().split()
    d.append([a, b])
    dt.append(b)
d.sort(key=lambda x: dt.count(x[1]))

print(" ".join([i[0] for i in d if dt.count(i[1]) == dt.count(d[-1][1])]))