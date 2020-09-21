from django.db import models

"""
Category
===========
title , slug

Tag
===========
title, slug

Post
===========
title, slug, author, content, created_at, image, views, category, tags 
"""


class Category(models.Model):

    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title


class Tag(models.Model):

    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):

    class Meta:
        ordering = ['-created_at']

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='author')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='Qty of views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title
