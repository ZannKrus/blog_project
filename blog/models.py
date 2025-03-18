from django.db import models
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    slug = models.SlugField("Слаг", max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Article(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("Слаг", max_length=200, unique=True)
    content = models.TextField("Содержимое")
    published_date = models.DateTimeField("Дата публикации", default=timezone.now)
    image = models.ImageField("Изображение", upload_to='articles/', blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name="Категория", on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug])
    
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name="Статья", on_delete=models.CASCADE, related_name='comments')
    author = models.CharField("Имя", max_length=80)
    content = models.TextField("Комментарий")
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    approved = models.BooleanField("Одобрен", default=True)

    def __str__(self):
        return f'Комментарий от {self.author}'
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


