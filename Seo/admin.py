from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone


# Register your models here.

from .models import *
from django.utils.text import slugify
# Register your models here.


def get_backlinks_for_domain(domain):
    return Backlink.objects.filter(da__gt=10, type='WpPostYorum').exclude(
        domainbacklink__domain=domain
    )
class DomainAdmin(admin.ModelAdmin):
    list_display = ("domain","YorumYazar","Yorum","BlogTitle","sahiplik",)
    actions = ['assign_backlinks']

    def assign_backlinks(self, request, queryset):
        for domain in queryset:
            backlinks = get_backlinks_for_domain(domain)
            domain_backlinks = [DomainBacklink(domain=domain, backlink=backlink, type='Beklemede') for backlink in
                                backlinks.iterator()]
            DomainBacklink.objects.bulk_create(domain_backlinks)

    assign_backlinks.short_description = "Seçili domainleri Blog Yorum backlink atama"


admin.site.register(Domain, DomainAdmin)





class BacklinkAdmin(admin.ModelAdmin):
    list_display = ("url","da","pa","spam_score","age","type")

admin.site.register(Backlink, BacklinkAdmin)


class BekleyenAdmin(admin.ModelAdmin):
    list_display = ("domain","backlink","Durum","yayin_tarihi")

admin.site.register(DomainBacklink, BekleyenAdmin)


class KategoriAdmin(admin.ModelAdmin):
    list_display = ("Title","slug","description","description_length","keywords","Aktif",)
    prepopulated_fields = {'slug': ('Title',)}
    search_fields = ("Title",)
    list_filter = ("Aktif",)
    list_editable = ("Aktif",)

    def description_length(self, obj):
        length = len(obj.description)
        if length <= 155:
            return format_html('<span style="color: green;">{}/155</span>', length)
        else:
            return format_html('<span style="color: red;">{}/155</span>', length)
    description_length.short_description = 'Desc-Len'

admin.site.register(PostKategori, KategoriAdmin)




class KontrolAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "kelime_sayisi", "meta_description", "hikayeyi_gor", "Post_Turu","Akibeti", "keywords", "Kaynak_Ana_Link", )
    search_fields = ("title",)
    list_filter = ("Akibeti", "Kaynak_Ana_Link", )
    list_editable = ("Post_Turu", "Akibeti", )

    def hikayeyi_gor(self, obj):
        return format_html('<a target="_blank" style="padding: 5px 10px; background-color: #198754; color: white; text-decoration: none; display: inline-block; text-align: center; border-radius: 5px;" href="/story-preview/{}">Post Gör</a>', obj.slug)

    hikayeyi_gor.short_description = 'Post'

admin.site.register(Kontrol, KontrolAdmin)



class MahsulAdmin(admin.ModelAdmin):
    list_display = ("Tarla_Link", "Mahsul_Link", "Akibeti", "Aciklama", "olusturma_tarihi", )
    search_fields = ("Tarla_Link",)
    list_editable = ("Akibeti",)
    list_filter = ("Akibeti", "Tarla_Link", )

admin.site.register(Mahsul, MahsulAdmin)



