from PIL import Image

# Görseli yükle
im = Image.open('Center.png')

# Boyutları yazdır
print(f"Genişlik: {im.width}px")
print(f"Yükseklik: {im.height}px")

# Her pikselin rengini al
pikseller = list(im.getdata())

# Her bir rengin piksel sayısını hesapla ve yazdır
piksel_sayilari = {}
for piksel in pikseller:
    if piksel[1] == 255:  # Yeşil rengin RGB değeri (0, 255, 0)
        if piksel in piksel_sayilari:
            piksel_sayilari[piksel] += 1
        else:
            piksel_sayilari[piksel] = 1

print(f"Toplam {len(piksel_sayilari)} farklı yeşil tonu bulundu.")
deger=0
for renk, sayi in piksel_sayilari.items():
    print(f"Renk {renk}: {sayi} piksel")
    deger +=sayi
print(deger)
