def sira():
    try:
        print("\nKitaplarımız\n \n")
        sirala = open("FinalProjem.txt")
        for i in sirala:
            print(i)
    except FileNotFoundError:
        print("Lütfen Txt Uzantılı Dosyayı İndirdiğinizden Emin Olun")
