def MyMathShower(*a):
  s = 0
  t = 1
  h = 2* a[0]
  for n in a:
    s += n
    t *= n
    h -= n
  return s, t , h

print(MyMathShower(10,4,1,1))