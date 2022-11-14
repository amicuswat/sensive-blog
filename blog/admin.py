from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('author', 'post',)
    raw_id_fields = ('post', 'author',)


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title',)
    raw_id_fields = ('author', 'tags', 'likes', )


admin.site.register(Tag)
