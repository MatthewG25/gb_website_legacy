from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('', views.intro, name='index'),
    path('part1/', views.part1, name='part 1'),
    path('part2a/', views.part2a, name='part 2a'),
    path('part2b/', views.part2b, name='part 2b'),
    path('part3/', views.part3, name='part 1'),
    path('part4/', views.part4, name='part 1'),
    path('part5/', views.part5, name='part 1'),
    path('conclusion/', views.conclusion, name='part 1')

]
