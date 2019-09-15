from django.db import models

from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(models.Model):
    titulo = models.CharField(
        max_length=27,
        blank=False,
        null=False,
    )

    sub_titulo = models.CharField(
        max_length=27,
    )

    thumb = models.ImageField(upload_to='thumbs/%Y/%m/%d')

    descricao = models.TextField(
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        max_length=20,
        blank=False,
        null=False
    )

    data_postagem = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    data_atualizacao = models.DateTimeField(
        blank=True,
        null=True,
    )

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    tags = TaggableManager()

    class Meta:
        verbose_name, verbose_name_plural = u"Post", u"Posts"

    def __str__(self):
        return "%s" % self.titulo

    objects = models.Manager()
