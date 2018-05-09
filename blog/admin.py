from django.contrib import admin
from .models import Article,Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    list_display_links = ["author"]

    class Meta:
        model = Article

admin.site.register(Comment)