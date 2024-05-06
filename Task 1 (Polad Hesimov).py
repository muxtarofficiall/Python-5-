#funksiya
class Qəhraman:
    status = "Şəhid"

    def __init__(self, derecesi, ad, soyad, yaş):
        self.derecesi = derecesi
        self.ad = ad
        self.soyad = soyad
        self.yaş = yaş
        
    def defn(self):
        return f"- {self.ad} {self.soyad} - II Fəxri Xyabamda dəfn olunmuşdur"

#obyekt
Milli_Qəhraman = Qəhraman("Polkovnik Leytinant", "Polad", "Həşimov", 47)

#obyekt print
print(f"Azərbaycanın Milli Qəhramanı {Milli_Qəhraman.derecesi} {Milli_Qəhraman.ad} {Milli_Qəhraman.soyad} {Milli_Qəhraman.yaş}-yaşında Tovuz əməliyyatları nəticəsində erməni silahlı qüvəlləri tərəfindən açılmış artereliyya atəşi nəticəsində qəhrəmancasına {Qəhraman.status}-olmuşdur:")
print(Milli_Qəhraman.defn())
