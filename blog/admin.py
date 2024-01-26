from django.contrib import admin
from blog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
  prepopulated_field = {"slug": ("title", )}
  list_display= ('published_at', 'slug')

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)