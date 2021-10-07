# Generated by Django 3.2.6 on 2021-10-06 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='download_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество скачиваний'),
        ),
        migrations.AddField(
            model_name='app',
            name='flag',
            field=models.BooleanField(choices=[(True, 'Верифицированное ПО'), (False, 'Неверифицированое ПО')], default=False, verbose_name='Верификация'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField(blank=True, verbose_name='О себе')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Город')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('avatar', models.ImageField(blank=True, upload_to='user_avatars/', verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default=None, max_length=20, null=True, verbose_name='Имя пользователя')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('app', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.app', verbose_name='Приложение')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
