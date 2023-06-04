# Basit deprem Uyari Sistem Uygulaması
Deprem Erken Uyarı Sistemi  
Dönem_projesi.py İçeriyi:  
* Bu programda kullancı olarak hesap oluşuturulabilir sonra giriş yapıp adminden gönderen uyarıları görünütülebilir.  
* kullancı olarak "Şifre Unuttum" seçip şifreni değiştirebilirsiniz.  
* Admin olarak giriş yapmak için "admin" ve "123456789+" sırayla adı ve şifre ile giriş yapabilirsiniz veya "Admin bilgileri değiştirmek" seçenek seçip yeni admin adını ve şifresi değiştirebilirsiniz.  
* Admin olarak kullancılar görüntülebilir ve Uyarı mesajları gönderilebilir.  
  
17_02_2023_Yeni_Dönem_projesi.py İçeriyi:  
* Bazı sorunları çözüldü.
* Renkler eklendi.
* Liste, Demet ve sözlük kullanıldı.  

01_06_2023_guncelleme.py İçeriyi:  
* Bu güncelleme ile save_credentials fonksiyonu, kullanıcı adını "Users" sütunu altında ve şifreyi "Password" sütunu altında yeni bir satır   olarak registered_users.xlsx Excel dosyasına ekleyecektir. mode='a' parametresi, dosyanın varsa mevcut verilerin sonuna eklemesini sağlar.  Buna ek olarak, header=True parametresi ile başlık satırının sadece ilk kez eklenmesi sağlanır.  
* df.index += 1: Bu satır, df veri çerçevesinin index sütununa 1 ekleyerek indeks değerlerini 1 artırır.  
* Böylece, view_registered_users fonksiyonu kullanıcıları görüntülerken indeks değerlerini 1'den başlatır.  
* Sonuç olarak, admin kullanıcı listesini görüntülerken kullanıcılar 1'den başlayarak numaralandırılır.  
Thanks for reading :)  
MOAYAD ALNADA  
201601716  
