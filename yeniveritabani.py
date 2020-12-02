"""
sayın kullanıcı eğer arama yapmak isterseniz arama fonksiyonuna .txt uzantılı dosyanızın ismini yazın eğer txt dosyanız
yoksa lütfen aşağıdaki fonksiyonu çalıştırarak oluşturun programı kapattığınız anda dosyanız açılacaktır ha bide lütfen
program ile aynı dizinde olsun. HAYIRLI UĞURLU
OLSUN sayemde txt uzantılı dosyanız olacak
Not : dosyalarımız iki tane veri alır eğer daha fazla isterseniz break komutlarını silin

"""

def yaz():
    isim_belirle = input("Lütfen Yeni Tabanımızın İsmini Belirleyelim : \n")
    metin = ".txt"
    yaz = open(isim_belirle + "{}" .format(metin), "w" )
    girdi_al = input("Lütfen Veri Girin")
    yaz.write(girdi_al)




    while True:
        yaz = open(isim_belirle + "{}" .format(metin), "a")
        yeni_girdi = input("Veri Girin")
        yaz.write("\n{}" .format(yeni_girdi))
        break


def farklidizin():
    dizinal = input("Kaydetmek İstediğiniz Dizinin Bağlantısını Paylaşın")
    isim_belirle = input("Lütfen Yeni Tabanımızın İsmini Belirleyelim : \n")
    metin = ".txt"
    isaret = "/"
    yaz = open(dizinal + "{}" .format(isaret) + isim_belirle +"{}".format(metin), "w")
    print(yaz)
    kaynakAl = input("Veri giriniz")
    yaz.write(kaynakAl)

    while True:
        yaz = open(dizinal + "{}".format(isaret) + isim_belirle + "{}".format(metin), "a")
        kaynakGirdi = input("Veri Girin")
        yaz.write("\n{}" .format(kaynakGirdi))
        break



def ara():

    try:
        dosya_ismi = input("Lütfen .txt Uzantılı Dosyanızın ismini Yazınız")

        isim_al = input("Aranan kelime")
        metin = ".txt"
        yaz = open(dosya_ismi + "{}" .format(metin))
        for i in yaz.readlines():
            if i.lower().find(isim_al) != -1:
                print(i)
    except FileNotFoundError:
        print("Ama Lütfen Söyledik Size Aynı Dizinde Olacak")

