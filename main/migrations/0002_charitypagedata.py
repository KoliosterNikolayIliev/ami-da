# Generated by Django 4.1.13 on 2024-12-07 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharityPageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_bg', models.CharField(blank=True, max_length=255, null=True)),
                ('heading_en', models.CharField(blank=True, max_length=255, null=True)),
                ('main_text_bg', models.TextField(blank=True, null=True)),
                ('main_text_en', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='images/')),
                ('embedded_video', models.TextField()),
                ('payment_heading_bg', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_heading_en', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_text_bg', models.TextField(blank=True, null=True)),
                ('payment_text_en', models.TextField(blank=True, null=True)),
                ('payment_info_bg', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_info_en', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Charity page data',
            },
        ),
    ]
