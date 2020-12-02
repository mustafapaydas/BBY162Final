from random import *
def kitapsec():
    try:
        oku = open("FinalProjem.txt")

        kitapsec = choice(oku.readlines())
        print(kitapsec)
    except FileNotFoundError:
        print("Lütfen Txt Uzantılı Dosyayı İndirdiğinizden Emin Olun")
