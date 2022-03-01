import time

girdi = int(input("Lütfen bir seçenek seçiniz:\n1) Araba ile gitme\n2) Yürüyerek gitme\nSeçiminiz: "))

if girdi == 1:
    a = int(input("Lütfen yolun uzunluğunu metre cinsinden giriniz: "))
    b = int(input("Lütfen gideceğiniz hızı giriniz (eğer bilmiyorsanız 60 yazabilirsiniz.): "))
    print("Hesaplanıyor...")
    time.sleep(1.5)
    sonuc = a // b
    print("Tahmini varış süreniz: {} dakika".format(sonuc))

if girdi == 2:
    m = 2
    a = int(input("Lütfen yürünecek mesafeyi metre cinsinden giriniz: "))
    print("Hesaplanıyor...")
    time.sleep(1.5)
    sonucc = a//85
    print("Tahmini varış süreniz: {} dakika".format(sonucc))

# python yuru.py
