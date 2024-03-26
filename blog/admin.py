from django.contrib import admin

# Register your models here.


from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ["img_preview"]


admin.site.register(Blog, BlogAdmin)
