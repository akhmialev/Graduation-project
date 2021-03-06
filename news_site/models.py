from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Вермя создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['time_create', 'title']


class Comment(models.Model):
    post = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE, verbose_name='Пост')
    name = models.CharField(max_length=180, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Текс')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Созданно')
    active = models.BooleanField(default=True, verbose_name='Опубликованно')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('created',)

    def __str__(self):
        return f'{self.name}'