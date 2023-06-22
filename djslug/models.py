from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import uuid

"""https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial"""
"""https://code.djangoproject.com/ticket/31725"""
"""https://docs.djangoproject.com/en/4.2/topics/files/"""


class Blog(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=200)
	body = models.TextField()
	body1 = models.TextField(blank=True)
	body2 = models.TextField(blank=True)
	cover = models.ImageField(upload_to='images/', blank=True, null=True)
	slug = models.SlugField(max_length=200, unique_for_date='published')
	published = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_post')


	def __str__(self):
		return self.title


class Comment(models.Model):
	text = models.TextField()
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text[:30] + "..."











