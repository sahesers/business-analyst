#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

boy  = float(input('Lütfen boyunuzu "metre" cinsinden giriniz...'))
kilo = float(input('Lütfen kilonuzu "kilogram" cinsinden giriniz...'))
VKİ= kilo / (boy * boy)
print("Vücut Kitle Endeksiniz", VKİ)