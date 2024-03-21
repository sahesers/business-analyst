#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

 
sayi1 = int(input("Lütfen Birinci Sayıyı Giriniz: "))
sayi2 = int(input("Lütfen İkinci Sayıyı Giriniz: "))
sayi3 = int(input("Lütfen Üçüncü Sayıyı Giriniz: "))

enBuyuk = max(sayi1, sayi2, sayi3)
print("En büyük değer:", enBuyuk)