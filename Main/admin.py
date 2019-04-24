from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *

class NewsAdmin(SummernoteModelAdmin):
    summer_note_fields = ('body', )

admin.site.register(News, NewsAdmin)
admin.site.register()
admin.site.register()
admin.site.register()
