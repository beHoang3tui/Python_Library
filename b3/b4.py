A = set(["An", "Binh", "Nam", "Long", "Ngoc", "Tu"])
B = set(["Binh", "Linh", "Nam", "Hai", "Long"])

# câu a Loại “Tu” ra khỏi danh sách
A.remove("Tu")
print(A)
print(B)

# câu b Thêm “Cuong” vào tập A
A.update(["Cuong"])
print(A)
print(B)

# câu c Tạo tập C chứa tất cả thành viên của tập A và tập B sao cho không trùng nhau
C = A.union(B)
print(C)

# câu d Tạo tập D chứa những thành viên thuộc tập A và B
D = A.intersection(B)
print(D)

# câu e Tạo tập E chứa những thành viên thuộc tập A nhưng không thuộc tập B
E = A - B
print(E)

# câu f Tạo tập F chứa những thành viên chỉ nằm trong tập A hoặc tập B
F = A.symmetric_difference(B)
print(F)
