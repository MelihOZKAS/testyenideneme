# Generated by Django 5.0.2 on 2024-03-15 14:22

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Seo", "0012_rename_name_domain_domain_domain_sahiplik"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mahsul",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Tarla_Link", models.URLField(blank=True, null=True)),
                ("Mahsul_Link", models.URLField(blank=True, null=True)),
                (
                    "Akibeti",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Tamamlandi", "Tamamlandi"),
                            ("Beklemede", "Beklemede"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("Aciklama", models.CharField(blank=True, max_length=255, null=True)),
                ("olusturma_tarihi", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name_plural": "Mahsuller",},
        ),
        migrations.CreateModel(
            name="PostKategori",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(blank=True, max_length=255)),
                ("slug", models.SlugField(blank=True, max_length=255)),
                ("H1", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("keywords", models.CharField(blank=True, max_length=255)),
                ("short_title", models.CharField(blank=True, max_length=255)),
                ("Aktif", models.BooleanField(default=False)),
                ("olusturma_tarihi", models.DateTimeField(auto_now_add=True)),
                ("guncelleme_tarihi", models.DateTimeField(auto_now=True)),
            ],
            options={"verbose_name_plural": "Post Kategori",},
        ),
        migrations.CreateModel(
            name="Kontrol",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("slug", models.CharField(blank=True, max_length=255, null=True)),
                ("h1", models.CharField(blank=True, max_length=255, null=True)),
                ("icerik", ckeditor.fields.RichTextField(blank=True, null=True)),
                (
                    "meta_description",
                    models.TextField(blank=True, verbose_name="Meta Açıklama"),
                ),
                (
                    "keywords",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Anahtar Kelimeler"
                    ),
                ),
                (
                    "Akibeti",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Salla", "Salla"),
                            ("Beklemede", "Beklemede"),
                            ("Tamamlandi", "Tamamlandi"),
                            ("Hazirla", "Hazirla"),
                            ("Yolda", "Yolda"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "Kaynak_Dili",
                    models.CharField(
                        blank=True,
                        choices=[("ENG", "ENG"), ("TR", "TR")],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("Kaynak_Linki", models.URLField(blank=True, null=True)),
                ("olusturma_tarihi", models.DateTimeField(auto_now_add=True)),
                (
                    "Post_Turu",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Seo.postkategori",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Kontrol",},
        ),
    ]
