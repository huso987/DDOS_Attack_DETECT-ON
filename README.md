
# BİRLEŞİK MAKİNE ÖĞRENMESİ  ALGORİTMALARIYLA  YAZILIM TANIMLI AĞLARA YAPILAN HİZMET DIŞI BIRAKMA SALDIRILARININ TESPİTİ 

Mininet emülatörü üzerinde birleşik model tabanlı bir Yazılım tanımlı 
ağda (YTA) hizmet dışı bırakma saldırılarının tespiti üzerine bir model geliştirilmiştir. 
Çalışmanın amacı, Yazılım tanımlı ağ  ortamında hizmet dışı bırakma  saldırılarının etkin bir 
şekilde tespit edilmesidir.İlk olarak, beş farklı kontrolcü kullanılarak çeşitli ağ topolojileri 
oluşturulmuş ve bu topolojiler üzerinde Hizmet dışı bırakma (HDB) saldırıları simüle 
edilmiştir. Bu simülasyonlar sonucunda, saldırı senaryoları ile beş farklı veri seti elde edilmiştir. 
Elde edilen bu veri setleri, model eğitimi için kullanılmıştır.Model eğitiminin ardından, 
CICDDoS2019   veri seti ve kendimizin ürettiği data set kullanılarak bir birleşik model 
geliştirilmiştir. Geliştirilen birleşik model, nb_classifier, PA_classifier, mlp_classifier, 
dt_classifier  ve xgb_classifier gibi farklı sınıflandırıcıların birleşiminden oluşan 
VotingClassifier ile gerçekleştirilmiştir. Modelin performansı çeşitli metrikler kullanılarak 
değerlendirilmiş ve sonuçlar, modelin hizmet dışı bırakma saldırılarını tespit etmede etkili 
olduğunu göstermiştir. Bu çalışma, yazılım tanımlı ağlarında hizmet dışı bırakma saldırılarının 
tespiti için yenilikçi ve etkili bir yaklaşım sunmaktadır.

# Confusion Matrix

![image](https://github.com/huso987/DDOS_Attack_DETECT-ON/assets/66470348/4a4d52fe-f7f0-4e10-b460-bc6fa9fd8b8e)




