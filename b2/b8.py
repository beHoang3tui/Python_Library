a = input('Nhập chuỗi : ')
d= a.count('1')
k=0
for i in range(len(a)):
  if(a.count('1', 0, i) == d/2):
    k= i
    break

print(a[:k],' ', a[k:])