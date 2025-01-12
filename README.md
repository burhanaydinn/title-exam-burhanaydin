## QE - Title Sınavı Projesi - Catchylabs

### Proje Hakkında:

Bu proje, **Testinium** terfi sınavı kapsamında web test otomasyon süreçlerini kapsayacak şekilde hazırlanmıştır. 
**Gauge** framework'ü kullanılarak BDD (Davranış Odaklı Geliştirme) yaklaşımı benimsenmiş, test senaryoları anlaşılır ve 
yönetilebilir hale getirilmiştir. Tarayıcılar arası test otomasyonu için **Selenium 4** tercih edilmiştir. 
Kodun sürdürülebilirliğini ve tekrar kullanılabilirliğini artırmak için **Singleton** tasarım deseni uygulanmıştır.

---

### Kullanılan Teknolojiler:

- **Selenium 4:** Tarayıcı otomasyonu için en son özellikler ve iyileştirmelerden yararlanıldı.
- **Java:** Temel programlama dili olarak tercih edildi.
- **Senaryo @Tag Yapılandırması:** Senaryoları etiketleme mekanizmaları ile kategorize edip, etiketlere dayalı seçici test yürütme sağlandı.
- **Gauge:** BDD (Davranış Odaklı Geliştirme) çerçevesi olarak kullanıldı.
- **Singleton Tasarım Deseni:** Kodun yeniden kullanılabilirliğini ve sürdürülebilirliğini artırmak için uygulandı.
- **Git:** Sürüm kontrolü ve işbirlikçi geliştirme için entegre edildi.
- **GaugeReport:** Ayrıntılı test yürütme raporları ve analizler için kullanıldı.

---

### Gereklilikler ve Bağımlılıklar:

- **Java (1.8)**
- **Maven** (Bağımlılık yönetimi için)
- **Git** (Sürüm kontrolü için)
- **Tarayıcılar:** Chrome, Firefox

---

### Sorun Giderme İpuçları:

- **Java Sürüm Hatası:**  Java (1.8) yüklü olduğundan emin olun.
- **Bağımlılık Hatası:** mvn clean install komutunu çalıştırarak eksik bağımlılıkları yükleyin.
- **Tarayıcı Uyumsuzluğu:** Kullanılan tarayıcının uyumlu olduğundan emin olun.

---

### Sonuçları İnceleyin:

Test çalıştırıldıktan sonra sonuç ve raporları görmek için:  
- `reports/html-report/index.html` dosyasını tarayıcınızda açarak test sonuçlarını görüntüleyebilirsiniz.

---

### Notlar:

- Bu README dosyası temel bilgileri içermektedir. Daha fazla ayrıntı için lütfen proje dosyalarına göz atın.
- Herhangi bir sorunuz veya sorununuz varsa, lütfen **[mail](mailto:burhan.aydin@testinium.com?subject=TitleExam%20Hk.)** adresinden benimle iletişime geçin.