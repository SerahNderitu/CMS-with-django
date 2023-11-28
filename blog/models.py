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


