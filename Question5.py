#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.


for i in range(100,1000):
    s = str(i)
    t = s[::-1]
    if s == t:
        print(s)