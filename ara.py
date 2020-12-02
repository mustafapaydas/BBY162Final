def arama():
    try:

        kitapİsmi = input("Lütfen Aramak İstediğiniz Kelimeyi Yazınız. :\n")

        arasin = open("FinalProjem.txt")
        for i in arasin.readlines():
            if i.lower().find(kitapİsmi) != -1:
                print(i)
            elif i.upper().find(kitapİsmi) != -1:
                print(i)

    except FileNotFoundError:
        print("Lütfen Txt Uzantılı Dosyayı İndirdiğinizden Emin Olun")




