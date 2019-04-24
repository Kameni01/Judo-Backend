from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', 'api_root'),
    path('news/', NewsList.as_view(), name='news-list'),
    path('news/<int:id>/', NewsDetail.as_view(), name='news-detail'),
    path('sportcard/', SportCardList.as_view(), name='sportcard-list'),
    path('sportcard/<int:id>', SportCardDetail.as_view(), name='sportcard-detail'),
    path('trenercard/', TrenerCardList.as_view(), name='trenercard-list'),
    path('trenercard/<int:id>', TrenerCardDetail.as_view(), name='trenercard-detail'),
    path('materials/', MaterialsList.as_view(), name='materials-list'),
    path('materials/<int:id>', MaterialsDetail.as_view(), name='materials-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])


#Возможно тут будет ошибка при конкатинации патернов.
#В случае ошибки переписать на новые стандарты
#Это дефолтные вьюхи для логина и логаута. Возможно пригодятся для авторизации
#и перенаправлении на админку
urlpatterns += patterns('',
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
