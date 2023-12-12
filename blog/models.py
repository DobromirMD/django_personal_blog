
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50
    )
    email = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Post(models.Model):


    def its_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.title

    title = models.CharField(
        max_length=150
    )
    excerpt = models.CharField(
        max_length=200
    )
    image = models.ImageField(
        upload_to="posts",
        null=True
    )
    date = models.DateTimeField(
        auto_now=True
    )
    slug = models.SlugField(
        unique=True,  # unique=True adds a index by default
        db_index=True,  # auto for slug field
    )
    content = models.TextField(
        validators=[
            MinLengthValidator(10)
        ]

    )
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True
    )
    tags = models.ManyToManyField(
        Tag
    )


class Comment(models.Model):
    user_name = models.CharField(
        max_length=120
    )
    user_email = models.EmailField()
    text = models.TextField(
        max_length=400
    )
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )