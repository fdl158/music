# Generated by Django 2.1.7 on 2019-02-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_img',
            field=models.ImageField(upload_to='song_img/%Y%m,', verbose_name='歌曲图片'),
        ),
    ]
