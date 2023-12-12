# Register your models here.


from blog.models import Post, Author, Tag, Comment
from django.contrib import admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ["author", "date", "tags"]
    list_display = ["title", "author", "date"]
    prepopulated_fields = {"slug": ("title",)}



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ["user_name", "post"]
