import random

oyunDurumu = True

while oyunDurumu:
    rastgele = random.randint(1,10)
    kalanHak = 5
    while True:
        if kalanHak > 0:
            try:
                tahmin = int(input("Sayıyı tahmin edin 1-100: "))
            except:
                print("Sayı gir lütfen")
                break
        else:
            print("Tebrikler kaldınız :))")
            break
        if tahmin != rastgele:
            kalanHak -= 1
            if tahmin > rastgele:
                print("Aşağı in! Kalan hakkınız {}".format(kalanHak))
            else:
                print("Yukarı çık! Kalan hakkınız {}".format(kalanHak))
        else:
            print("Maalesef bildiniz")
            break
    kontrol = input("Tekrar oynamak ister misiniz E-H ")
    if kontrol == "E" or kontrol == "e":
        oyunDurumu = True
    else:
        oyunDurumu = False
        print("Oyun bitti iyi günler")
