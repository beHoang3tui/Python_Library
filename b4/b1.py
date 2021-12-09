a = input()
s = a.index('(')
print(' '.join(a[s+1:len(a)-1].split(',')))