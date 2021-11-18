from django.contrib import admin

from .models import Description, Title

class DescriptionInLine(admin.StackedInline):
    model = Description
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [DescriptionInLine]

admin.site.register(Title, PostAdmin)
