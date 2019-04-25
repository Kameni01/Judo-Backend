from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])


#Возможно тут будет ошибка при конкатинации патернов.
#В случае ошибки переписать на новые стандарты
#Это дефолтные вьюхи для логина и логаута. Возможно пригодятся для авторизации
#и перенаправлении на админку
# urlpatterns += patterns('',
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# )
