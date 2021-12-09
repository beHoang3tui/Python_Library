a = input()
s = 0
for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        if a.count(a[i:j]) >= 2:
            s = max(s, j-i+1)
print(s)