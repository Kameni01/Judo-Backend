from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *

# class NewsAdmin(SummernoteModelAdmin):
#     summer_note_fields = ('body', )

admin.site.register(News)
admin.site.register(SportCard)
admin.site.register(Achievements)
admin.site.register(Education)
admin.site.register(Qualification)
admin.site.register(AcademicDegree)
admin.site.register(TrenerCard)
admin.site.register(Materials)
admin.site.register(VideoAlbums)
admin.site.register(VideoGalerry)
