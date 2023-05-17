from colorama import init, Fore, Style
init()
kullancilar = {}
adminler = ["admin","123456789+"]
mesajlar = []
uyarilar = []
i = 1
back = False
anamenu = False

print("Dönem Projesi 'MOAYAD ALNADA' 201601716")
input_color = Fore.MAGENTA
menu_color = Fore.CYAN
print_fcolor = Fore.RED
print_tcolor = Fore.GREEN

colored_input = lambda prompt: input(f"{input_color}{prompt}{Style.RESET_ALL}")
falsed_print = lambda text: print(f"{print_fcolor}{text}{Style.RESET_ALL}")
trued_print = lambda text: print(f"{print_tcolor}{text}{Style.RESET_ALL}")

def colored_input(prompt):
    return input(f"{input_color}{prompt}{Style.RESET_ALL}")
def falsed_print(text):
    print(f"{print_fcolor}{text}{Style.RESET_ALL}")
def trued_print(text):
    print(f"{print_tcolor}{text}{Style.RESET_ALL}")


def ana_menu():
    print(f"{menu_color}\n1. Üye Ol")
    print("2. Giriş Yap")
    print("3. Şifremi Unuttum")
    print("4. Admin Girişi")
    falsed_print("5. Uygulamadan Çık")

def besinci_secim():
    print(f"\033[33m1. *{len(uyarilar)}* Mesajınız var\033[0m")
    falsed_print("2. Çıkış yap")

def ikinci_menu():
    print(f"{menu_color}\n1. Admin bilgileriyle giriş yapmak")
    print("2. Admin bilgilerini değiştirmek")
    print("\033[90m3. Geri\033[0m")

def ucuncu_menu():
    print(f"{menu_color}1. Kullanıcıların bilgileri")
    print("2. Kullanıcılara uyarı gönder")
    falsed_print("3. Çıkış yap")

def dorduncu_menu():
    print(f"{menu_color}\n1. Admin adını değiştirmek")
    print("2. Admin şifresini değiştirmek")
    print("\033[90m3. Geri\033[0m")

while True:
    ana_menu()
    secim = colored_input("Seçiminiz (1-5): ")

    if secim == "1":
        while True:
            kullanici_adi = colored_input("\nKullanıcı adınızı giriniz: ")
            if kullanici_adi in kullancilar:
                falsed_print("\n---Kullanıcı adı zaten kullanılmış. Lütfen başka bir kullanıcı adı deneyin---\n",falsed_print)
            else:
                break
        while True:
            sifre = colored_input("Şifre belirleyiniz: ")
            if len(sifre) >= 6:
                kullancilar[kullanici_adi] = sifre
                trued_print("\n---Kaydınız başarıyla oluşturuldu---\n")
                break
            else:
                falsed_print("\n---Şifreniz en az 6 karakter olmalıdır---\n")

    elif secim == "2":
        kullanici_adi = colored_input("\nKullanıcı adı: ")
        sifre = colored_input("Şifreniz: ")
        if kullanici_adi in kullancilar and kullancilar[kullanici_adi] == sifre:
            trued_print(f"\n-----------\nHoş geldiniz {kullanici_adi}" )
            trued_print("-----------\n")
            while True:
                besinci_secim()
                secim5 = colored_input("Seçiminiz (1-2): ")
                if secim5 == "1":
                    if not uyarilar:
                        print("\033[33m\n---Herhangi bir uyarınız yok---\n\033[0m")
                        
                    else:
                        print("\033[33m\n*** Yeni uyarınız var ***\n\033[0m")
                        i = 1
                        for uyari in uyarilar:                            
                            print(f"\033[33m{i}. {uyari}\033[0m")
                            print("   ----")
                            i += 1
                elif secim5 == "2":
                    break
                else:
                    falsed_print("Geçersiz seçim!\n")
        else:
            falsed_print("\n---Şifreniz veya kullanıcı adınız hatalıdır---\n")

    elif secim == "3":
        kullanici_adi = colored_input("\nKullanıcı adı: ")
        while True:
            if kullanici_adi in kullancilar:
                yeni_sifre = colored_input("Yeni şifre belirleyiniz: ")
                if len(yeni_sifre) >= 6:
                    if kullancilar[kullanici_adi] == yeni_sifre:
                        falsed_print("\n---Yeni şifreniz eski şifrenizle aynı olamaz. Lütfen başka bir şifre belirleyiniz---\n")
                    else:
                        kullancilar[kullanici_adi] = yeni_sifre
                        trued_print("\n---Yeni şifreniz kaydedildi---\n")
                        break
                else:
                    falsed_print("\n---Lütfen şifre en az 6 karakter olmalıdır---\n")
            else:
                falsed_print("\n---Bu kullanıcı adı kayıtlı değildir---\n")

    elif secim == "4":
        while True:
            try:
                if secim3 == "3":
                    break
            except:
                ikinci_menu()
                secim2 = colored_input("Seçiminiz (1-3): ")
                if secim2 == "1":
                    admin_adi = colored_input("\nAdmin adı: ")
                    admin_sifre = colored_input("Şifre: ")
                    if admin_adi in adminler[0] and adminler[1] == admin_sifre:
                        trued_print("\nAdmin olarak başarıyla giriş yaptınız")
                        while True:
                            ucuncu_menu()
                            secim3 = colored_input("Seçiminiz (1-3): ")
                            if secim3 == "1":
                                if not kullancilar:
                                    trued_print("\n---Herhangi bir kullanıcı yok---\n")
                                else:
                                    print("\n")
                                    for i, kullanici in enumerate(kullancilar, start=1):
                                        print(f"\033[33m{i}. Kul.adı: {kullanici} : Şifre: {kullancilar[kullanici]}\033[0m")
                                    print("\n")
                            elif secim3 == "2":
                                uyari_mesaji = colored_input("Uyarı mesajını yazın: ")
                                uyarilar.append(uyari_mesaji)
                                trued_print("\n---Mesajınız kullanıcılara iletilmiştir---\n")
                            elif secim3 == "3":
                                break
                            else:
                                falsed_print("Geçersiz seçim!\n")
                    else:
                        falsed_print("\n---Admin adı veya şifre hatalıdır---")
                        break
                elif secim2 == "2":
                    while True:
                        dorduncu_menu()
                        secim4 = colored_input("Seçiminiz (1-3): ")
                        if secim4 == "1":
                            yeni_admin_adi = colored_input("Lütfen yeni admin adını yazınız: ")
                            if not yeni_admin_adi:
                                falsed_print("Admin adını boş bırakamazsınız")
                            else:
                                adminler[0] = yeni_admin_adi
                                trued_print("\n---Admin adı başarıyla değiştirildi---\n")
                                break
                        elif secim4 == "2":
                            admin_adi = colored_input("Admin Adını giriniz: ")
                            if admin_adi == adminler[0]:
                                yeni_admin_sifre = colored_input("Lütfen yeni şifre giriniz: ")
                                if len(yeni_admin_sifre) >= 10:
                                    if adminler[1] in yeni_admin_sifre:
                                        falsed_print("\n---Güvenliğiniz için yeni şifreniz eski şifrenizle aynı olamaz.---\n")
                                    else:

                                        adminler[1] = yeni_admin_sifre
                                        trued_print("\n---Admin şifresi başarıyla değiştirildi---\n")
                                        break
                                else:
                                    falsed_print("\n---Admin şifresi en az 10 karakter olmalıdır---\n")
                            else:
                                falsed_print("\n---Bu admin adı kayıtlı değildir---\n")
                        elif secim4 == "3":
                            break
                        else:
                            falsed_print("Geçersiz seçim!\n")
                elif secim2 == "3":
                    break
                else:
                    falsed_print("Geçersiz seçim!\n")

    elif secim == "5":
        falsed_print("\nUygulamadan çıkılıyor.....")
        break

    else:
        falsed_print("Geçersiz seçim!\n")
            
