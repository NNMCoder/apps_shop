# Generated by Django 3.2.6 on 2021-10-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='star.png', upload_to='news_avatars/', verbose_name='Заставка'),
        ),
    ]