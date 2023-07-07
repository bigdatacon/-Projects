from django.urls import include, path
from rest_framework import routers
# from polls import views
from polls.views import FileuplViewSet, FilmWorkViewSet
# from movies import views
from movies.views import FilmWorkMovieViewSet, MovieList, filmworkmovie_list, index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.urls import include, path

router = routers.DefaultRouter()
# router.register(r'fileupload', views.FileuplViewSet)
# router.register(r'filmwork', views.FilmWorkViewSet)

router.register(r'fileupload', FileuplViewSet)
router.register(r'filmwork', FilmWorkViewSet)

#Блок для таблицы с фильмами 1000+
router.register(r'FilmWorkMovie', FilmWorkMovieViewSet)




urlpatterns = [
    # path('polls/question/', include('polls.urls')),
    path('movies/', include('movies.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    #Блок для таблицы с фильмами 1000+
    # path('film_workmovie', views.index, name='film_workmovie'),
    # path('filmworkmovie_list/', views.filmworkmovie_list),
    # path('filmworkmovie_view/', views.MovieList.as_view()),
    # path('index/', views.index),

    path('film_workmovie', index, name='film_workmovie'),
    path('filmworkmovie_list/', filmworkmovie_list),
    path('filmworkmovie_view/', MovieList.as_view()),
    path('index/', index),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

