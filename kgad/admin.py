from django.contrib import admin
from .models import AdGene
from .models import AdArticle

# Register your models here.
@admin.register(AdGene)
class AdGendAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    search_fields = ['id']
    list_per_page = 20
    # exclude = ['is_virtual']
    list_filter = ['id']

@admin.register(AdArticle)
class AdArticleAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    search_fields = ['id']
    list_per_page = 20
    # exclude = ['is_virtual']
    list_filter = ['id']