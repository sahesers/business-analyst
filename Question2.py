#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

Güncelmaas=0
maas=input("Mevcut Maasi Gir : ")
zam=input("Zam Oranı(%) : ")
Güncelmaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamli Maaş :",Güncelmaas)