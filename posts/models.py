import os
from django.db import models

from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.dispatch import receiver


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
        auto_now_add=True,
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


@receiver(models.signals.post_delete, sender=Post)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Remove o arquivo quando o objeto Post
    correspondente for deletado
    """
    if instance.thumb:
        if os.path.isfile(instance.thumb.path):
            os.remove(instance.thumb.path)


@receiver(models.signals.pre_save, sender=Post)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Remove o arquivo antigo quando o objeto Post
    correspondente for atualizado com uma nova imagem
    """
    if not instance.pk:
        return False

    try:
        old_file = Post.objects.get(pk=instance.pk).thumb
    except Post.DoesNotExist:
        return False

    new_file = instance.thumb
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
