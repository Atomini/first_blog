# Generated by Django 3.2.4 on 2021-06-12 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('post_slug', models.SlugField(max_length=200, unique=True, verbose_name='Url')),
                ('published_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('category', models.CharField(choices=[('science', 'наука'), ('sport', 'спорт')], max_length=100, verbose_name='Категория')),
                ('into_image', models.ImageField(blank=True, upload_to='posts/static/posts', verbose_name='Картинка тизера')),
                ('into_text', models.CharField(max_length=100, verbose_name='Текст тизера')),
                ('post_text', models.TextField(verbose_name='Текст поста')),
                ('moderated', models.BooleanField(default=False, verbose_name='Прошел модерацию')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField(max_length=250, verbose_name='текст котентария')),
                ('text_comment_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата публикации коментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.blogposts')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('author_slug', models.SlugField(max_length=200, unique=True, verbose_name='Url')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
    ]
