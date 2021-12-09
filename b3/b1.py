def xd10(n):
  n = str(n)
  if ('1' in n ):
    return 1
  elif ('0' in n ):
    return 1
  return 0
def ss10(n,k):
  n = str(n)
  k = str(k)
  s = []
  g = [] 
  for i in range(len(n)):
    if ( n[i] == '0' or n[i] == '1' ):
      s.append(i)
  for i in range(len(k)):
    if ( k[i] == '0' or k[i] == '1'):
      g.append(i)
  if( s == g):
    return 1
  else:
    return 0    

arr = list(map(str, input().split()))
arr2 = []
for i in range(len(arr)):
    if xd10(arr[i]) == 1:
        arr2.append(arr[i])
for i in range(len(arr2)):
    for j in range(i+1,len(arr2)):
        if ss10(arr2[i],arr2[j])==1:
            arr2.remove(arr2[j])
print(arr2)


