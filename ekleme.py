def ekle():
    try:
        ekleme = open("FinalProjem.txt", "a")
        kitapbagis = input("lütfen eser adı, yazar adı, tarih(yyyy)olarak giriniz : ")
        ekleme.write("{} \n" .format(kitapbagis))

    except FileNotFoundError:
        print("Lütfen Txt Uzantılı Dosyayı İndirdiğinizden Emin Olun")
