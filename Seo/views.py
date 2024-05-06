from django.shortcuts import render,HttpResponse,get_object_or_404,reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import re
from django.views import View
from .models import *
import json
from django.db import IntegrityError
from django.http import JsonResponse
from django.utils.html import strip_tags
from html import unescape


def home3(request):
    user_agent = request.META.get('HTTP_USER_AGENT').lower()

    if 'amphtml' in user_agent or 'mobile' in user_agent or 'safari' in user_agent in user_agent:
        # Mobil cihaz ise AMP sayfasına yönlendir
        return render(request, 'amp/blog.amp.html')
    else:
        # Masaüstü cihaz ise normal sayfaya yönlendir
        return HttpResponse(f'Sitemiz Şu an Yapımda')






def create_unique_title_slug(title):
    slug = slugify(title)
    unique_slug = slug
    unique_title = title
    num = 1
    while Kontrol.objects.filter(slug=unique_slug).exists() or Kontrol.objects.filter(title=unique_title).exists():
        unique_slug = '{}-{}'.format(slug, num)
        unique_title = '{} {}'.format(title, num)
        num += 1
    return unique_title, unique_slug


def home(request):
    user_agent = request.META['HTTP_USER_AGENT']

    # Mobil cihazları tanımlayan bir regex deseni
    mobile_regex = r".*(iphone|mobile|androidtouch)"

    # Kullanıcı ajanını kontrol edin
    if re.match(mobile_regex, user_agent, re.I):
        return render(request, 'amp/blog.amp.html')
    else:
        return HttpResponse(f'Sitemiz Şu an Yapımda')



class StoryPreviewView(View):
    def get(self, request, *args, **kwargs):
        story = Kontrol.objects.get(slug=kwargs['slug'])

        # Veritabanından bilgileri çek
        title = story.title
        h1 = story.h1
        keywords = story.keywords
        description = story.meta_description

        # İçeriği oluştur
        content = f"Title: {title}\n\n <br> H1: {h1}\n\n <br> Keywords: {keywords}\n\n <br> Description: {description}\n\n <br> {story.icerik} \n\n  "

        return HttpResponse(content)


def Enderun(request, post_slug):
    user_agent = request.META.get('HTTP_USER_AGENT').lower()
    PostEndrun = get_object_or_404(Kontrol, slug=post_slug)

    title = PostEndrun.title
    H1 = PostEndrun.h1
    description = PostEndrun.meta_description
    keywords = PostEndrun.keywords

    context = {
        'title': title,
        'H1': H1,
        'description': description,
        'keywords': keywords,
        'PostEndrun': PostEndrun,
    }

    if 'amphtml' in user_agent or 'mobile' in user_agent or 'safari' in user_agent in user_agent:
        # Mobil cihaz ise AMP sayfasına yönlendir
        return render(request, 'amp/blog.amp.html', context)
    else:
        # Masaüstü cihaz ise normal sayfaya yönlendir
        return HttpResponse(f'Sitemiz Şu an Yapımda')


def EnderunNew(request, post_slug):
    user_agent = request.META.get('HTTP_USER_AGENT').lower()
    PostEndrun = get_object_or_404(Kontrol, slug=post_slug)

    title = PostEndrun.title
    H1 = PostEndrun.h1
    description = PostEndrun.meta_description
    keywords = PostEndrun.keywords

    context = {
        'title': title,
        'H1': H1,
        'description': description,
        'keywords': keywords,
        'PostEndrun': PostEndrun,


    }

    if 'amphtml' in user_agent or 'mobile' in user_agent or 'safari' in user_agent in user_agent:
        # Mobil cihaz ise AMP sayfasına yönlendir
        return render(request, 'amp/new-enderun.amp.html', context)
    else:
        # Masaüstü cihaz ise normal sayfaya yönlendir
        return HttpResponse(f'Sitemiz Şu an Yapımda')


@csrf_exempt
def mahsulyakala(request):
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            for item in data:
                Main_Link = item.get('Main_Link')
                Post_Link = item.get('Post_Link')
                try:
                    mahsulkayit = Mahsul(Tarla_Link=Main_Link, Mahsul_Link=Post_Link, Akibeti='Beklemede')
                    mahsulkayit.save()
                except IntegrityError:
                    continue  # Bu satırı ekledim.
            return JsonResponse({"message": "Başarılı"})
        else:
            return JsonResponse({"error": "Geçersiz Content-Type başlığı"}, status=400)
    else:
        return JsonResponse({"method": request.method, "headers": dict(request.headers)})

@csrf_exempt
def mahsullistesicek(request):
    if request.method == 'POST':
        tarla_link = request.POST.get('Tarla_Link')
        mahsul_list = Mahsul.objects.filter(Tarla_Link=tarla_link).order_by('-olusturma_tarihi')[:150]
        mahsul_links = "|".join([mahsul.Mahsul_Link for mahsul in mahsul_list])
        return HttpResponse(mahsul_links)
    else:
        return HttpResponse("Geçersiz istek", status=400)


@csrf_exempt
def mahsulcek(request):
    if request.method == 'POST':
        tarla_link = request.POST.get('Tarla_Link')
        mahsul_cek = Mahsul.objects.filter(Tarla_Link=tarla_link, Akibeti="Beklemede").order_by('olusturma_tarihi').first()
        if mahsul_cek is not None:
            mahsul_cek.Akibeti = "Tamamlandi"
            mahsul_cek.save()
            return HttpResponse(mahsul_cek.Mahsul_Link)
        else:
            return HttpResponse("Mahsul bulunamadı", status=404)
    else:
        return HttpResponse("Geçersiz istek", status=400)


@csrf_exempt
def post_add(request):
    if request.method == 'POST':
        # Gelen POST isteğindeki değerleri alın
        title = request.POST.get('title')
        h1 = request.POST.get('h1')
        Post_Turu = request.POST.get('Post_Turu')
        icerik = request.POST.get('icerik')
        meta_description = request.POST.get('meta_description')
        key = request.POST.get('keywords')
        Kaynak_Linki = request.POST.get('Kaynak_Linki')
        Kaynak_Dili = request.POST.get('Kaynak_Dili')
        Kaynak_Ana_Link = request.POST.get('Kaynak_Ana_Link')
        # Kaynak_Ana_Link değerini kullanarak ilgili BackEndDomain nesnesini bulun
        Kaynak_Ana_Link_Gelen = BackEndDomain.objects.get(Kaynak_Ana_link=Kaynak_Ana_Link)

        Post_Turu_Gelen = PostKategori.objects.get(Title=Post_Turu)

        title, slug = create_unique_title_slug(title)
        siir_masal = Kontrol(title=title,  slug=slug, h1=h1, Post_Turu=Post_Turu_Gelen, icerik=icerik, keywords=key, meta_description=meta_description, Akibeti="Beklemede", Kaynak_Linki=Kaynak_Linki, Kaynak_Dili=Kaynak_Dili, Kaynak_Ana_link=Kaynak_Ana_Link_Gelen)
        siir_masal.save()
        if siir_masal.id is None:
            return HttpResponse("Post kaydedilemedi.")
        else:
            return HttpResponse("Post başarıyla kaydedildi. ID: " + str(siir_masal.id))



@csrf_exempt
def ai_cek(request):
    if request.method == 'POST':
        field = request.POST.get('field')  # field parametresi, hangi alana göre filtreleme yapılacağını belirtir (ör. 'kidsStories')
        kontrols = Kontrol.objects.filter(Akibeti='Kullan', **{field: 'Kullan'})
        if kontrols.exists():
            random_kontrol = kontrols.order_by('?').first()
            Sonucu = f"{random_kontrol.pk}|={random_kontrol.title}|={random_kontrol.h1}|={random_kontrol.Post_Turu}|={random_kontrol.meta_description}|={random_kontrol.keywords}|={random_kontrol.icerik}|={random_kontrol.Kaynak_Linki}"
            return HttpResponse(Sonucu)
        else:
            return JsonResponse({'error': 'Belirtilen koşullara uygun bir kontrol nesnesi bulunamadı.'})



@csrf_exempt
def ai_cek_Alt_Baslik_Cek(request):
    if request.method == 'POST':
        Tur = request.POST.get('Tur')
        kontrols = Kontrol.objects.filter(Akibeti=Tur)
        if kontrols.exists():
            random_kontrol = kontrols.order_by('?').first()
            random_kontrol.Akibeti = "YoldaAltBaslik"
            random_kontrol.save()
            Sonucu = f"{random_kontrol.pk}|={random_kontrol.icerik}"
            return HttpResponse(Sonucu)
        else:
            return JsonResponse({'error': 'Belirtilen koşullara uygun bir kontrol nesnesi bulunamadı.'})





@csrf_exempt
def ai_add(request):
    if request.method == 'POST':
        # Gelen POST isteğindeki değerleri alın
        ZekaOzet = request.POST.get('ZekaOzet')
        icerik = request.POST.get('icerik')
        GelenID = request.POST.get('GelenID')


        Postislem = Kontrol.objects.get(pk=GelenID)
        Postislem.ozet = ZekaOzet
        Postislem.sonucPost = icerik
        Postislem.Akibeti = "Tamamlandi"
        Postislem.save()

        if Postislem.id is None:
            return HttpResponse("Post kaydedilemedi.")
        else:
            return HttpResponse("Şükürler Olsun Post başarıyla kaydedildi. ID: " + str(Postislem.id))
@csrf_exempt
def ai_alt_baslik_add(request):
    if request.method == 'POST':
        # Gelen POST isteğindeki değerleri alın
        GelenID = request.POST.get('GelenID')
        Alt = request.POST.get('Alt')



        Postislem = Kontrol.objects.get(pk=GelenID)
        Postislem.AltBasliklar = Alt
        Postislem.Akibeti = "AltBaslikKontrol"
        Postislem.save()

        if Postislem.id is None:
            return HttpResponse("Post kaydedilemedi.")
        else:
            return HttpResponse("Şükürler Olsun Post başarıyla kaydedildi. ID: " + str(Postislem.id))