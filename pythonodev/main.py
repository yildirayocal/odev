kullanıcı="YILDIRAY"#Kullanıcı adını belirledik.
parola="1234"#Şifreyi belirledik.
while (True):#Döngünün sürdürülmesi için yazılan satır.
    kadi=input("Kullanıcı adı : ")#Kullanıcıya kullanıcı adını soruyoruz.
    ksifre=input("Şifre : ")#Kullanıcıya şifre soruyoruz.
    if kullanıcı==kadi and parola==ksifre:#Kullanıcı adını ve parolasını veri tabanında ki bilgilerle karşılaştırıyor.
        print("Hoşgeldiniz ",kadi)#Kullanıcı adı ve şifre doğru ise giriş yapıcak.
        print("Başarılı bir şekilde giriş yapıldı.")
        son=input("Çıkış yapmak için ENTER tuşuna basınız.")
        break
    elif kullanıcı!=kadi and parola==ksifre:#Kullanıcı adı yanlış ise bu satır çalışacak.
        print("Kullanıcı adınızı yanlış girdiniz")

    elif kullanıcı==kadi and parola!=ksifre:#Şifre yanlış ise bu satır çalışacak.
        print("Şifrenizi yanlış girdiniz")
        print("Şifrenizi değiştirmek istermisiniz?(E/H)")#Şifre değiştirme işlemi için sorgu yapıyor.

        cevap=input()
        if cevap=='E':#cevap evet ise çalışacak kodlar
            yeniparola=input("Yeni parola : ")#Yeni parola belirleme işlemi yapılıyor.
            print("Lütfen Bekleyiniz.")
            parola=yeniparola#Yeni parola eski parola ile değiştiriliyor.
            print("Şifreniz değiştirme işlemi paşarılı.")
            print("Lütfen tekar giriş yapınız.")
        elif cevap=='e':#cevap evet ise çalışacak kodlar
            yeniparola=input("Yeni parola : ")#Yeni parola belirleme işlemi yapılıyor.
            print("Lütfen Bekleyiniz.")
            parola=yeniparola#Yeni parola eski parola ile değiştiriliyor.
            print("Şifreniz değiştirme işlemi paşarılı.")
            print("Lütfen tekar giriş yapınız.")
        else:#cevap hayır ise çalışıcak kodlar.
            print("Şifre değiştirme işlemi iptal edildi.")
            print("Lütfen tekrar giriş yapmayı deneyiniz.")
    else:#Kullanıcı adı ve şifre yanlış ise çalışacak kodlar.
        print("Giriş yapma işlemi başarısız.Lütfen tekrar deneyiniz.")

