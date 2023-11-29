from django.db import models

from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Delete")
)


class Posts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    meta_description = models.CharField(max_length=300, default="new post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = 'Posts'

    def __str__(self):  # manage models from the terminal
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = 'Messages'

    def __str__(self):
        return '{} ({})'.format(self.name, self.email)


