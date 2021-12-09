a = input("Nhập mảng :")
a = a.replace("‘", '')
a = a.replace("’", '')
a = a.replace(',', '')

# print(a)
s = []

for i in range(len(a)):
  if(int(a[i]) %2 ==0):
    s.append(int(a[i]))
for i in range(len(a)):
  if(int(a[i]) %2 !=0):
    s.append(int(a[i]))
print(s)