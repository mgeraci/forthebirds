from django.contrib import admin

from creations.models import Book, RadioProgram


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'year_published',
    )
    filter_horizontal = ('species',)


class RadioProgramAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'original_air_date',
    )
    filter_horizontal = ('species',)


admin.site.register(Book, BookAdmin)
admin.site.register(RadioProgram, RadioProgramAdmin)
