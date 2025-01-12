QE Automation Case - Calculator
===============================
Created by burhanaydinn on 9.01.2025
tags:prod

Senaryo 1: Yatırım Hesaplaması
------------------------------
tags: Calculator, Catchylabs, Web, YatirimHesaplama
* Catchylabs web sayfasi acilir
* Catchylabs login icin "burhan.aydin" ve sifre ile yapilir
* Hesap makinesi acilir
* Yatirim tutari girilir
* Carpi ikonuna tiklanir
* Faiz orani girilir
* Esittir ikonuna tiklanir
* Toplama ikonuna tiklanir
* Yatirim tutari girilir
* Esittir ikonuna tiklanir
* Sonuc kontrol ve kayit edilir
* "HesaplamaSonucu" ile kaydedilen değer ile "105" değerini karşılaştır

Senaryo 2: Aylık Bütçe Hesaplaması
----------------------------------
tags: Calculator, Catchylabs, Web, AylikButceHesaplamasi
* Catchylabs web sayfasi acilir
* Catchylabs login icin "burhan.aydin" ve sifre ile yapilir
* Hesap makinesi acilir
* Gelir tutari girilir
* Cikarma ikonuna tiklanir
* Gider tutari girilir
* Esittir ikonuna tiklanir
* Sonuc kontrol ve kayit edilir
* "HesaplamaSonucu" ile kaydedilen değer ile "200" değerini karşılaştır

Scenario 3: Günlük Gider Takibi
-------------------------------
tags: Calculator, Catchylabs, Web, GunlukGiderTakibi
* Catchylabs web sayfasi acilir
* Catchylabs login icin "burhan.aydin" ve sifre ile yapilir
* Hesap makinesi acilir
* Gunluk gider yemek girilir
* Toplama ikonuna tiklanir
* Gunluk gider ulasim girilir
* Toplama ikonuna tiklanir
* Hesaplama alaninda ikinci toplama ikonu kontrol edilir
* Gunluk gider kahve girilir
* Esittir ikonuna tiklanir
* Sonuc kontrol ve kayit edilir
* "HesaplamaSonucu" ile kaydedilen değer ile "35" değerini karşılaştır

Scenario 4: Yıllık Yatırım Hesaplaması
--------------------------------------
tags: Calculator, Catchylabs, Web, YillikYatirimHesaplamasi
* Catchylabs web sayfasi acilir
* Catchylabs login icin "burhan.aydin" ve sifre ile yapilir
* Hesap makinesi acilir
* Yillik yatirim tutari girilir
* Carpi ikonuna tiklanir
* Yillik faiz orani girilir
* Esittir ikonuna tiklanir
* Toplama ikonuna tiklanir
* Yillik yatirim tutari girilir
* Esittir ikonuna tiklanir
* Sonuc kontrol ve kayit edilir
* "HesaplamaSonucu" ile kaydedilen değer ile "208" değerini karşılaştır

Scenario 5: Kısa Vadeli Yatırım Hesaplaması
-------------------------------------------
tags: Calculator, Catchylabs, Web, KisaVadeliYatirimHesaplamasi
* Catchylabs web sayfasi acilir
* Catchylabs login icin "burhan.aydin" ve sifre ile yapilir
* Hesap makinesi acilir
* Kisa vadeli faiz oranı girilir
* Carpi ikonuna tiklanir
* Yatirimin süresi girilir
* Esittir ikonuna tiklanir
* Toplama ikonuna tiklanir
* Faiz formulu bir butonuna tiklanir
* Esittir ikonuna tiklanir
* Carpi ikonuna tiklanir
* Kisa vadeli yatirim tutari girilir
* Esittir ikonuna tiklanir
* Sonuc kontrol ve kayit edilir
* "HesaplamaSonucu" ile kaydedilen değer ile "507.5" değerini karşılaştır