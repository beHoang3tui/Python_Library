def ktra(str1, str2):
    m = len(str1)
    n = len(str2)

    j = 0
    i = 0
    while (i < n and j < m):
        if (str1[j] == str2[i]):
            j += 1
        i += 1

    return (j == m)

def timChuoi(d, str1):
    str = ""
    length = 0

    for word in d:
        if (length < len(word) and ktra(word, str1)):
            str = word
            length = len(word)

    return str

str= ["TRẺ TRÂU"];
str1 = input("Nhập 1 chuỗi: ")
if (timChuoi(str, str1)== "TRẺ TRÂU"):
    print("TRẺ TRÂU");
else:
    print("Không TRẺ TRÂU");