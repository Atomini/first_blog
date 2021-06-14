from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify
from django.urls import reverse
from django.utils import timezone


class BlogPosts(models.Model):
    CATEGORIES = [
        ('science', 'Наука'),
        ('sport', 'Спорт'),
    ]
    title = models.CharField("Название", max_length=100, blank=False, unique=True)
    post_slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="Url")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_time = models.DateTimeField("Дата публикации", default=timezone.now)
    category = models.CharField("Категория", choices=CATEGORIES, max_length=100)

    into_image = models.ImageField("Картинка тизера", upload_to='images/', blank=True, default="images/wallhaven"
                                                                                               "-4yjzd4.jpg")
    into_text = models.CharField("Текст тизера", max_length=100, blank=False)

    post_text = models.TextField("Текст поста", blank=False)

    moderated = models.BooleanField("Прошел модерацию", default=False, blank=False)
    published = models.BooleanField("Опубликован", default=False, blank=False)

    def __str__(self):
        return self.title + " - " + str(self.author)

    def get_absolute_url(self):
        # return "/%s/" % self.post_slug
        return '/'

    def save(self, *args, **kwargs):
        self.post_slug = slugify(self.title)
        super(BlogPosts, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'


class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_name = models.CharField("Имя автора", blank=False, null=False, max_length=100)
    author_slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name="Url")

    def __str__(self):
        return self.author_name

    def get_absolute_url(self):
        return "author/%s/" % self.author

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = 'Авторы'


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey('BlogPosts', on_delete=models.CASCADE, default=None)
    text_comment = models.TextField("текст котентария", max_length=250)
    text_comment_time = models.DateTimeField("дата публикации коментария", default=timezone.now)

    def get_absolute_url(self):
        # if self.post_id.post_slug:
        #     return "/%s/" % self.post_id.post_slug
        # else:
        #     return reverse("home")
        return reverse("home")

    def __str__(self):
        return str(self.author) + " - " + str(self.post_id.title)

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = 'Коментарии'
