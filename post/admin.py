from django.contrib import admin
from .models import Post

# Create Saliha Atiþ

class PostAdmin(admin.ModelAdmin):

    list_display = ["baslik", "yayim_tarihi", "slug"]
    list_display_links = ["yayim_tarihi"]
    list_filter = ["baslik", "yayim_tarihi"]
    search_fields = ["baslik", "metin"]


    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
