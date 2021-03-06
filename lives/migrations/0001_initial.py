# Generated by Django 2.1.5 on 2019-01-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日程')),
                ('image', models.ImageField(blank=True, upload_to='lives', verbose_name='画像(任意）')),
                ('venue', models.CharField(max_length=100, verbose_name='会場')),
                ('venue_url', models.URLField(blank=True, verbose_name='会場URL（任意）')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='イベント名（任意）')),
                ('detail', models.TextField(blank=True, verbose_name='詳細（任意）')),
            ],
        ),
    ]
