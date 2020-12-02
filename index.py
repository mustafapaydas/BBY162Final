"""
Hocam isteğiniz üzere fonksiyon çağırma adlarını dosya ismi . fonksiyon ismi olarak editledim
"""

from listeleme import *
from ara import *
from ekleme import *
from yeniveritabani import *
from kitapal import *

sira()

while True:
    print("                    Arama Yap(A) - Kitap Ekle (K) Yeni Veri Tabanı Oluşturma (Y) Başka Bir Txt uzantılı Dosyada Arama Yapma (B) \n \n")
    print("                                                                   Veya Günün Şanslı Kitabını Seçin (G) \n")
    istek = input("Lütfen yapmak istediğiniz işlemi seçin  \n")

    if "a" == istek.lower():
        arama()

    elif "k" == istek.lower():
        ekle()
        print("İşleminiz Tamamlandı")
    elif "y" == istek.lower():
        fark = input("Yeni Dizinde Txt Dosyası Açmak İstermisiniz E/H : ")
        if fark.lower() == "e":
            farklidizin()

        else:
            yaz()

    elif "b" == istek.lower():
        ara()
    elif "g" == istek.lower():
        kitapsec()
    else:
        print("Yazdığınız Karakteri tekrar incelermisiniz.")
