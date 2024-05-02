# Generated by Django 5.0.2 on 2024-02-24 21:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Seo", "0009_rename_yazar_domain_blogtitle_domain_yorumyazar"),
    ]

    operations = [
        migrations.AddField(
            model_name="backlink",
            name="guncelleme_tarihi",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="backlink",
            name="olusturma_tarihi",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="domain",
            name="guncelleme_tarihi",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="domain",
            name="olusturma_tarihi",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="domainbacklink",
            name="guncelleme_tarihi",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="domainbacklink",
            name="olusturma_tarihi",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="domainbacklink",
            name="yayin_tarihi",
            field=models.DateTimeField(
                blank=True, help_text="Postanın yayınlanacağı tarih ve saat", null=True
            ),
        ),
    ]
