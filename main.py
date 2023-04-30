import datetime
from smtplib import SMTP

if __name__ == '__main__':
    toplanti = input("Toplantı,Etkinlik Adı Giriniz :")
    print(toplanti)
    gun =int(input("Toplantı,Etkinlik Günü Giriniz :"))
    print(gun)
    if (gun<0 or gun>31):
        print ("Hatalı Bir Gün Girdiniz, Saat 0,31 Arası Olmalıdır.")
        gun = int(input("Toplantı,Etkinlik Günü Giriniz :"))
        print(gun)
    ay =int(input("Toplantı,Etkinlik Ayını Giriniz :"))
    print(ay)
    if (ay<0 or ay>12):
        print ("Hatalı Bir Ay Girdiniz, Saat 0,12 Arası Olmalıdır.")
        ay = int(input("Toplantı,Etkinlik Ayını Giriniz :"))
        print(ay)
    yil =int(input("Toplantı,Etkinlik Yılını Giriniz :"))
    print(yil)
    if (yil < 2023):
        print("Hatalı Bir Yıl Girdiniz,Yıl 2023 veya daha büyük Olmalıdır.")
        yil = int(input("Toplantı,Etkinlik Yılını Giriniz :"))
        print(yil)
    saat = int(input("Toplantı,Etkinlik Saatini Giriniz :"))
    print(saat)
    if (saat<0 or saat>23):
        print ("Hatalı Bir Saat Girdiniz, Saat 0,23 Arası Olmalıdır.")
        saat = int(input("Toplantı,Etkinlik Saatini Giriniz :"))
        print(saat)
    dakika =int(input("Toplantı,Etkinlik Dakikasını Giriniz :"))
    print(dakika)
    if (dakika < 0 or dakika > 60):
        print("Hatalı Bir Dakika Girdiniz, Saat 0,60 Arası Olmalıdır.")
        dakika = int(input("Toplantı,Etkinlik Dakikasını Giriniz :"))
        print(dakika)
    tarih=datetime.datetime(yil,ay,gun,saat,dakika)
    print (tarih)
    katilimci=int(input("Toplantı,Etkinliğe Kaç Kişi Katılacağını Giriniz :"))
    print (katilimci)
    if (katilimci<=0):
        print ("Hatalı Kişi Sayısı Girdiniz, 0dan Büyük Olmalıdır.")
        katilimci = int(input("Toplantı,Etkinliğe Kaç Kişi Katılacağını Giriniz :"))
        print(katilimci)
# class
class Etkinlik:
    # class attributes
    # constructor (yapıcı metod)
    def __init__(toplanti,tarih,katilimci):
        # object attributes
        etkinlik.toplanti = toplanti
        etkinlik.tarih = tarih
        etkinlik.katilimci = katilimci
        print('init metodu çalıştı.')

    # methods


# object (instance)
p1 = Etkinlik(toplanti=toplanti,tarih=tarih,katilimci=katilimci)

# updating
p1.etkinlik = 'cey'

# accessing object attributes
print(f'p1:  toplanti: {p1.toplanti} :tarih: {p1.tarih} :katilimci: {p1.katilimci}')


print(p1)
print(type(p1))
x = ("Toplantının Adı: " + etkinlik + "\n" + "Toplantı Tarihi: " + str(
    tarih) + "\n" + "Toplantıya Katılacak Kişi Sayısı: " + str(katilimci))
print (x)