from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog")
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

    def img_preview(self):
        return mark_safe('<img src="{url}" width="200" />'.format(url=self.image.url))
