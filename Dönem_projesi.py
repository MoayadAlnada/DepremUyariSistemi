kullancilar = {}
Sifre = ""
adminadi = "admin"
adminSifre = "123456789+"
mesaj = 0
Uyari = []
back = False
anamenu = False
i=1

print("Dönem Projesi 'MOAYAD ALNADA' 201601716")
def ana_menu():
    print("\n1. Üye Ol")
    print("2. Giriş Yap")
    print("3. Şifremi Unuttum")
    print("4. Admin girişi ")
    print("5. Uygulamadan Çık")

while True:
    anamenu = False
    ana_menu()
    secim = input("Seçiminiz (1-5): ")

    if secim == "1":
        kullanciadi = input("\nkullancı adınızı giriniz: ")
        while True:
            Sifre = input("Şifre belirleyiniz: ")
            if len(Sifre) >= 6:
                kullancilar[kullanciadi] = Sifre
                print("\n---Kaydınız başarıyla oluşturuldu---\n")
                break
            else:
                print("\n---Şifreniz en az 6 karakter olmalıdır---\n")

    elif secim == "2":
        while True:
            kullanciadi = input("\nkullancı adı: ")
            Sifre = input("Şifreniz: ")
            if kullanciadi in kullancilar: 
                if kullancilar[kullanciadi] == Sifre:
                    print("\n-----------\nHoş geldiniz",kullanciadi)
                    print("-----------\n")
                    giriste_kullnanci = kullanciadi
                    def besinci_secim():
                        print(f"1. *{len(Uyari)}* Mesajların var")
                        print("2. Çıkış yap")    
                    while True:
                        besinci_secim()
                        secim5 = input("Seçiminiz (1-2): ")
                        if secim5 == "1":
                            if not Uyari:
                                print("\n---Her hangi bir uyarınız yoktur.---\n")
                            else:
                                print("\n*** Yeni uyarınız var. ***")
                                for u in Uyari:
                                    print("\n    ----\n")
                                    print(f"{i}. ",u)
                                    i+=1   
                                    
                        elif secim5 == "2":
                            
                            break
                        else:
                            print("Geçersiz seçim!\n")  

                        
                    break
                else:
                    print("\n---Şifreniz veya kullancı adınızı Hatalıdır---\n")
            else:
                print("\n---Şifreniz veya kullancı adınızı Hatalıdır---\n")
      
    elif secim == "3":
        kullanciadi = input("\nKullancı adı: ")
        while True:
            if kullanciadi in kullancilar:
                Yeni_Sifre = input("Yeni Şifre belirleyiniz: ")
                if len(Yeni_Sifre) >= 6:
                    if Yeni_Sifre == kullancilar[kullanciadi]:
                        print("\n---Yeni şifreniz eski şifrenizle aynı olamaz. Lütfen başka bir şifre belirleyiniz---\n")
                    else:
                        kullancilar[kullanciadi] = Yeni_Sifre
                        print("\n---Yeni şifreniz kaydedilmiştir---\n")
                        break
                    
                else:
                    print("\n---lütfen şifre en az 6 karakter olmalıdır---\n")
            else:
                print("\n---Bu Kullancı adı kayıtlı değildir---\n")
                break    
    
    elif secim == "4":
        
        def ikinci_menu():
            print("\n1. Admin bilgileriyle giriş yapmak")
            print("2. Admin bilgileri değiştirmek")
            print("3. Geri")
            
        while True and anamenu == False:
            back = False
            ikinci_menu()
            secim2 = input("Seçiminiz (1-3): ")
            if secim2 == "1":
                while True:
                    if anamenu == True:
                        break
                    adminadi = input("\nAdmin adi: ")
                    adminSifre = input("Şifre: ")
                    if adminadi == adminadi and adminSifre == adminSifre:
                        print("^^Admin olarak giriş yaptınız^^\n")
                        def ucuncu_menu():
                            print("1. Kullanıcıların bilgileri")
                            print("2. Kullanıcılara bir uyarı gönder")
                            print("3. Çıkış yap")
                        while True:
                            ucuncu_menu()
                            secim3 = input("Seçiminiz (1-3): ")
                            if secim3 == "1":
                                if not kullancilar:
                                    print("\n---Her hangi bir kullancı yoktur.---\n")
                                    break
                                else:
                                    for i,kullanci in enumerate(kullancilar):
                                            print("{}. {}".format(i+1, kullanci))
                                    print("\n")
                            elif secim3 == "2":
                                    uyari = input("Uyarı mesajını yazın: ")
                                    print("\n---Mesajınız kullanıcılara iletilmiştir.---\n")
                                    Uyari.append(uyari)
                            elif secim3 == "3":
                                anamenu = True
                                break
                            
                                
                            else:
                                print("Geçersiz seçim!\n")
              
                    else:
                        print("Admin adı veya şifre hatalıdır")
                        break
            elif secim2 == "2":
                def dorduncu_menu():
                    print("\n1. Admin adını değiştirmek")
                    print("2. Admin şifresi değiştirmek")
                    print("3. Geri")
                while True and back == False:
                    dorduncu_menu()
                    secim4 = input("Seçiminiz (1-3): ")
                    
                    if secim4 == "1": 
                        while True:                     
                            yeni_adminadi = input("Lütfen yeni Admin adını yazınız: ")
                            
                            
                            if not yeni_adminadi:
                                print("Admin adını boş bırakamazsınız")
                                
                                
                            else:
                                yeni_adminadi == adminadi
                                print("\n---Admin adı başarıyla değiştirilmiştir---\n")
                                
                                back = True
                                break
                    elif secim4 == "2":
                        while True:
                            yeni_adminSifre = input("Lütfen yeni şifre giriniz: ")
                            if len(yeni_adminSifre) > 9:
                                if yeni_adminSifre == adminSifre:
                                    print("Güvenliğiniz için yeni şifreniz eski şifrenizle aynı olamaz.")
                                else:
                                    yeni_adminSifre == adminSifre
                                    print("\n---Yeni şifreniz kaydedilmiştir---\n")
                                    back = True
                                    break    
                            else:
                                print("\n---Şifreniz en az 10 karakter olmalıdır---\n")
                                
                    elif secim4 == "3":
                        break
                    else:
                        print("Geçersiz seçim!\n")
            elif secim2 == "3":
                break
                
            
            else:
                print("Geçersiz seçim!\n")
                           
        
    elif secim == "5":
        quit() 
          
    else:
        print("Geçersiz seçim!\n")
    
