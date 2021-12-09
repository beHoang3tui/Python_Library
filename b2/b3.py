# câu a
d = 10
while True:
  s = input()
  if(len(s)> d):
    break

print(s[1:6])

# câu b
h = input()
print("Chuyển về chữ hoa :", h.upper())
print("Chuyển về chữ thường :", h.lower())
print(h.replace('b', 'g'))

# câu c

k ='hElLo-mY-NAMe-iS-SuZIe'
k = k.lower()
k = k.replace('-',' ')
k = k.title()
print(k)