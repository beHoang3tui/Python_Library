a = list(map(int, input("Nhập mảng :").split()))
k = int(input('Nhập K :'))
d=0
for i in range(0, len(a)):
  for j in range(i+1, len(a)):
    if(a[i]+a[j]==k):
      d +=1
    
print(d)