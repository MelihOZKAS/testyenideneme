from django.db import models
from ckeditor.fields import RichTextField



model_tipi = (
    ("BlogSeri1", "BlogSeri1"),
    ("WpPostYorum", "WpPostYorum"),
)

sahiplik_tipi = (
    ("Bizim", "Bizim"),
    ("Müşteri", "Müşteri"),
)


durum_tipi = (
    ("Beklemede", "Beklemede"),
    ("işlemde", "işlemde"),
    ("OK", "OK"),
)




class Domain(models.Model):
    domain = models.URLField()
    sahiplik = models.CharField(max_length=40, choices=sahiplik_tipi,blank=True)
    YorumYazar = models.TextField(blank=True)
    Yorum = models.TextField(blank=True)
    BlogTitle = models.TextField(blank=True)
    Blogcontent = models.TextField(blank=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.domain
    class Meta:
        verbose_name_plural = "1-Domain"

class Backlink(models.Model):
    url = models.URLField()
    da = models.IntegerField()
    pa = models.IntegerField()
    spam_score = models.IntegerField()
    age = models.IntegerField()
    type = models.CharField(max_length=40, choices=model_tipi,blank=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.url
    class Meta:
        verbose_name_plural = "1-Backlink"

class DomainBacklink(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    backlink = models.ForeignKey(Backlink, on_delete=models.CASCADE)
    Durum = models.CharField(max_length=40, choices=durum_tipi, blank=True)
    yayin_tarihi = models.DateTimeField(null=True, blank=True, help_text="Postanın yayınlanacağı tarih ve saat")
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('domain', 'backlink',)

        verbose_name_plural = "1-DomainBacklink"


class BackEndDomain(models.Model):
    Title = models.CharField(max_length=255, blank=True)
    Kaynak_Ana_link = models.CharField(max_length=600, blank=True, null=True, unique=True)
    class Meta:
        verbose_name_plural = "2-BackEndDomain"
    def __str__(self):
        return self.Title











class PostKategori(models.Model):
    Title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    H1 = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    keywords = models.CharField(max_length=255,blank=True)
    short_title = models.CharField(max_length=255, blank=True)
    Aktif = models.BooleanField(default=False)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "2-Post Kategori"
    def __str__(self):
        return self.Title



class Kontrol(models.Model):
    kontrol = [
        ('Beklemede', 'Beklemede'),
        ('AltBaslikYap', 'AltBaslikYap'),
        ('AltBaslikKontrol', 'AltBaslikKontrol'),
        ('YoldaAltBaslik', 'YoldaAltBaslik'),
        ('MakaleYap', 'MakaleYap'),
        ('YoldaMakale', 'YoldaMakale'),
        ('MakaleKontrol', 'MakaleKontrol'),
        ('KullanimaHazir', 'KullanimaHazir'),
        ('Tamamlandi', 'Tamamlandi'),


    ]


    islem = [
        ('Kontrol', 'Kontrol'),
        ('Kullan', 'Kullan'),
        ('Kullanıldı', 'Kullanıldı'),
        ('Kullanma', 'Kullanma'),
    ]



    Dili = [
        ('ENG', 'ENG'),
        ('TR', 'TR'),
        ('De', 'DE'),
        ('İtaly', 'İtaly'),
        ('Espanyol', 'Espanyol'),
        ('France', 'France'),
    ]

    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True,blank=True)
    h1 = models.CharField(max_length=255,blank=True, null=True)
    Post_Turu = models.ForeignKey(PostKategori, null=True, on_delete=models.SET_NULL)
    AltBasliklar = models.TextField(blank=True, verbose_name="Alt Başlıklar")
    icerikGelen = RichTextField(null=True, blank=True)
    icerikmain = RichTextField(null=True, blank=True)
    icerik2 = RichTextField(null=True, blank=True)
    icerik3 = RichTextField(null=True, blank=True)
    icerik4 = RichTextField(null=True, blank=True)
    icerik5 = RichTextField(null=True, blank=True)
    icerik6 = RichTextField(null=True, blank=True)
    icerik7 = RichTextField(null=True, blank=True)
    icerik8 = RichTextField(null=True, blank=True)
    icerik9 = RichTextField(null=True, blank=True)
    icerik10 = RichTextField(null=True, blank=True)
    ozet = models.TextField(blank=True, verbose_name="Özet")
    faq = models.TextField(blank=True, verbose_name="Faq")

    meta_description = models.TextField(blank=True, verbose_name="Meta Açıklama")
    keywords = models.CharField(max_length=255,blank=True,verbose_name="Anahtar Kelimeler")
    Akibeti = models.CharField(max_length=255, choices=kontrol, null=True, blank=True)
    Kaynak_Dili = models.CharField(max_length=255, choices=Dili, null=True, blank=True)
    Kaynak_Linki = models.URLField(blank=True, null=True)
    Kaynak_Ana_link = models.ForeignKey(BackEndDomain, blank=True, null=True, on_delete=models.SET_NULL)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    cocukmasali = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    kidsStories = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    yuksekteknoloji = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    hamilelik = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    bayanlaraozel = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    ailerehberi = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    kadinsorunlari = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    kadinvehayat = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    makyajvemoda = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    annebak = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    kadinlaricin = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    tiklahadi = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    siteniz = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")
    ekli = models.CharField(max_length=255, choices=islem, null=True, blank=True, default="Kontrol")



    class Meta:
        verbose_name_plural = "2-Kontrol"
    def __str__(self):
        return self.title

    def kelime_sayisi(self):
        return len(self.icerik.split())



class Mahsul(models.Model):
    kontrol = [
        ('Tamamlandi', 'Tamamlandi'),
        ('Beklemede', 'Beklemede'),
    ]
    Tarla_Link = models.URLField(blank=True, null=True)
    Mahsul_Link = models.URLField(blank=True, null=True, unique=True)
    Akibeti = models.CharField(max_length=255, choices=kontrol, null=True, blank=True)
    Aciklama = models.CharField(max_length=255, blank=True, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "2-Mahsuller"



