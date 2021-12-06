# Generated by Django 3.2.6 on 2021-12-06 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, default='star.png', upload_to='avatars/', verbose_name='Заставка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата загрузка')),
                ('file', models.FileField(upload_to='files/', verbose_name='Файл')),
                ('flag', models.BooleanField(choices=[(True, 'Верифицированное ПО'), (False, 'Неверифицированое ПО')], default=False, verbose_name='Верификация')),
                ('download_count', models.PositiveIntegerField(default=0, verbose_name='Количество скачиваний')),
                ('version', models.CharField(default='', max_length=10, null=True, verbose_name='Версия')),
                ('requirements', models.TextField(default='', null=True, verbose_name='Системные требования')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScreenshotsApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, upload_to='files/', verbose_name='Файлы')),
                ('app', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='shop.app', verbose_name='Скриншоты')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default=None, max_length=50, null=True, verbose_name='email')),
                ('information', models.TextField(blank=True, verbose_name='О себе')),
                ('city', models.CharField(blank=True, max_length=30, verbose_name='Город')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('avatar', models.ImageField(blank=True, default='star.png', upload_to='user_avatars/', verbose_name='Аватар')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('position', models.CharField(default='', max_length=100, null=True, verbose_name='Должность')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, default='star.png', upload_to='news_avatars/', verbose_name='Заставка')),
                ('annotation', models.TextField(default='', max_length=300, null=True, verbose_name='Аннотация')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('object_id', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Дата создания комментарий')),
                ('is_child', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_children', to='shop.comments', verbose_name='Родительский комментарий')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to='shop.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='app',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
