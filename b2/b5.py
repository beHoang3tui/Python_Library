n = int(input('Nhập N : '))

def sum(n):
  d= 0 
  while(n!=0):
    s = n % 10
    n = int(n/10)
    d += s
  return d

if(n<10):
  print(n)
else:
  while(n>=10):
    n=sum(n)
  else:
    print(n)

