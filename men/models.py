from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


# Create your models here.


class Men(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug",                           validators=[
                               MinLengthValidator(5, message="Мінімум 5 символів"),
                               MaxLengthValidator(100, message="Максимум 100 символів"),
                           ])
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Фото")
    content = models.TextField(blank=True, verbose_name="Текст статті")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час зміни")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Математика"
        verbose_name_plural = "Математики"
        ordering = ['-time_create']
        indexes = [models.Index(fields=['-time_create'])]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})



