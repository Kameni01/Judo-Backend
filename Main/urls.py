from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('news/', NewsList.as_view(), name="news-list"),
    path('news/<int:id>', NewsDetail.as_view(), name="news-detail"),
    path('sportcard/', SportCardList.as_view(), name="sportcard-list"),
    path('sportcard/<int:id>', SportCardDetail.as_view(), name="sportcard-detail"),
    path('achiv/<int:id>', AchievementsDetail.as_view(), name="achievements-detail"),
    path('trenercard/', TrenerCardList.as_view(), name="trenercard-list"),
    path('trenercard/<int:id>', TrenerCardDetail.as_view(), name="trenercard-detail"),
    path('materials/', MaterialsList.as_view(), name="materials-list"),
    path('materials/<int:id>', MaterialsDetail.as_view(), name="materials-detail"),
    path('v-albums/', VideoAlbumsList.as_view(), name="videoalbums-list"),
    path('v-albums/<int:id>', VideoAlbumsDetail.as_view(), name="videoalbums-detail"),
    path('v-gallery/', VideoGalerryList.as_view(), name="videogallery-list"),
    path('v-gallery/<int:id>', VideoGalerryDetail.as_view(), name="videogallery-detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])


#Возможно тут будет ошибка при конкатинации патернов.
#В случае ошибки переписать на новые стандарты
#Это дефолтные вьюхи для логина и логаута. Возможно пригодятся для авторизации
#и перенаправлении на админку
# urlpatterns += patterns('',
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# )
