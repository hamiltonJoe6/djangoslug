from django.contrib import admin
from . import models

from djslug.models import Comment

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }


admin.site.register(Comment)
