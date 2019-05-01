from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *

class NewsAdmin(SummernoteModelAdmin):
    list_display = ("title", 'created', "news_type")
    summer_note_fields = ('text', )
    list_editable = ("news_type", )
    search_fields = ("title", )


class MaterialsAdmin(SummernoteModelAdmin):
    list_display = ("title", "created", "type")
    summer_note_fields = ('text', 'comment')
    list_editable = ("type", )
    search_fields = ("title", )


class SportCardAdmin(SummernoteModelAdmin):
    list_display = ("name", "family", "birthday")
    search_fields = ("name", "family")
    summer_note_fields = ('description', )



class AchievementsAdmin(SummernoteModelAdmin):
    list_display = ("title", 'medal', 'owner')
    list_editable = ("owner", "medal")
    search_fields = ("title", 'owner')



class TrenerCardAdmin(SummernoteModelAdmin):
    list_display = ("name", "family", "patronymic", 'education',
                    'qualification', 'academic_degree')
    list_editable = ('education', 'qualification', 'academic_degree')
    search_fields = ("name", "family", "patronymic")




class VideoGalleryAdmin(SummernoteModelAdmin):
    list_display = ("title", "created", 'album')
    list_editable = ('album', )
    search_fields = ("title", "album")



class PhotoGalleryAdmin(SummernoteModelAdmin):
    list_display = ("title", "created", 'album')
    list_editable = ('album', )
    search_fields = ("title", "album")
    # exclude = ('photo_s', )



admin.site.register(News, NewsAdmin)
admin.site.register(SportCard, SportCardAdmin)
admin.site.register(Achievements, AchievementsAdmin)
admin.site.register(Education)
admin.site.register(Qualification)
admin.site.register(AcademicDegree)
admin.site.register(TrenerCard, TrenerCardAdmin)
admin.site.register(Materials, MaterialsAdmin)
admin.site.register(VideoAlbums)
admin.site.register(VideoGallery, VideoGalleryAdmin)
admin.site.register(PhotoAlbums)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
