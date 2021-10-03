from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    hex_regex = RegexValidator(
        regex=r'^#([A-Fa-f0-9]{6})$',
        message='Enter a valid hexfigure: e.g. "ff0022"'
    )
    color = models.CharField(
        max_length=7,
        validators=[hex_regex],
        unique=True
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=15)
    quantity = models.PositiveSmallIntegerField()
    measurement_unit = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    picture = models.ImageField(
        upload_to='api/',
        blank=True,
        null=True,
        verbose_name='фото'
    )
    description = models.TextField()
    ingredient = models.ManyToManyField('Ingredient')
    tag = models.ManyToManyField('Tag')
    cooking_time = models.PositiveSmallIntegerField()
    pub_date = models.DateTimeField('Pub date', auto_now_add=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.name


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
        verbose_name='пользователь')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        verbose_name='автор')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [models.UniqueConstraint(
            fields=['user', 'author'], name='unique_follow')]
