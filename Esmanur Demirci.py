

print(" ESMA DEMİRCİNİN YEMEK TARİFLERİ UYGULAMASINA HOŞGELDİNİZ !")

print("TÜRKÇE KARAKTER HATASI ALINABİLİR, BU SORUNLA KARŞILAŞIRSANIZ LÜTFEN TÜRKÇE KARAKTER KULLANMADAN GİRİNİZ")


kayıt = open("yemeklistesi.txt", "w") 
kayıt.write(input(  "Yemek Adı Giriniz = " )) 
kayıt.write(input( "Yemek Tarifi Giriniz = " ))
kayıt.close()

dosya = open("yemeklistesi.txt","r",encoding="utf-8")
oku = dosya.read()
print("Yemek Adı ve Tarifiniz = " ,oku)