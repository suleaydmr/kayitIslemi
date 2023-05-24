# Sulenur Aydemir-22210202013

class Ogrenci:
    def __init__(self, ad, numara, boy):
        self.ad = ad
        self.numara = numara
        self.boy = boy

# Ogrenci listesini oluştur
ogrenciler = []

# Kullanıcı arayüzü döngüsü
while True:
    print("1 - Kayıt ekle")
    print("2 - Kayıt değiştir")
    print("3 - Kayıt listele")
    print("4 - Öğrenci Sayısı")
    print("5 - En büyük boy")
    print("6 - En küçük boy")
    print("7 - Boyların toplamı")
    print("8 - Boyların ortalaması")
    print("9 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        ad = input("Öğrenci Adı: ")
        numara = input("Öğrenci Numarası: ")
        boy = input("Öğrenci Boyu: ")
        ogrenci = Ogrenci(ad, numara, boy)
        ogrenciler.append(ogrenci)
        print("Kayıt eklendi.\n")

    elif secim == "2":
        if len(ogrenciler) == 0:
            print("Kayıtlı öğrenci yok.\n")
        else:
            indeks = int(input("Değiştirmek istediğiniz kaydın indis numarasını girin: "))
            if indeks >= 0 and indeks < len(ogrenciler):
                ad = input("Yeni öğrenci adı: ")
                numara = input("Yeni öğrenci numarası: ")
                boy = input("Yeni öğrenci boyu: ")
                ogrenci = Ogrenci(ad, numara, boy)
                ogrenciler[indeks] = ogrenci
                print("Kayıt değiştirildi.\n")
            else:
                print("Geçersiz indis numarası.\n")

    elif secim == "3":
        if len(ogrenciler) == 0:
            print("Kayıtlı öğrenci yok.\n")
        else:
            print("Kayıtlı öğrenciler:")
            for indeks, ogrenci in enumerate(ogrenciler):
                print("Indis:", indeks)
                print("Öğrenci Adı:", ogrenci.ad)
                print("Öğrenci Numarası:", ogrenci.numara)
                print("Öğrenci Boyu:", ogrenci.boy)
                print("------------")

    elif secim == "4":
        print("Öğrenci Sayısı:", len(ogrenciler), "\n")


    elif secim == "5":
        if len(ogrenciler) == 0:
            print("Kayıtlı öğrenci yok.\n")
        else:
            max_boy = max(ogrenciler, key=lambda ogrenci: float(ogrenci.boy))

            print("En büyük boy:")

            print("Öğrenci Adı:", max_boy.ad)

            print("Öğrenci Numarası:", max_boy.numara)

            print("Öğrenci Boyu:", max_boy.boy, "\n")
    elif secim == "6":
        if len(ogrenciler) == 0:
            print("Kayıtlı öğrenci yok.\n")
        else:
            min_boy = min(ogrenciler, key=lambda ogrenci: float(ogrenci.boy))
            print("En küçük boy:")
            print("Öğrenci Adı:", min_boy.ad)
            print("Öğrenci Numarası:", min_boy.numara)
            print("Öğrenci Boyu:", min_boy.boy, "\n")

    elif secim == "7":
        if len(ogrenciler) == 0:
            print("Kayıtlı öğrenci yok.\n")
        else:
            toplam_boy = sum(float(ogrenci.boy) for ogrenci in ogrenciler)
            print("Boy Toplamı:", toplam_boy, "\n")

    elif secim == "8":
        if len(ogrenciler) == 0:
            print("Kayıtlı öğrenci yok.\n")
        else:
            ortalama_boy = sum(float(ogrenci.boy) for ogrenci in ogrenciler) / len(ogrenciler)
            print("Boy Ortalaması:", ortalama_boy, "\n")

    elif secim == "9":
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.\n")