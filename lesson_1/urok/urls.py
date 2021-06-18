from django.urls import path
from . import views
from .views import Oquch


urlpatterns = [
    path('', views.index, name='home'),
    path('pupil/', views.pupil, name='pupil'),
    path('classroom/', views.classroom, name='classroom'),
    path('royxat/', views.royxat, name='royxat'),
    path('sinflar/', views.sinflar, name='sinflar'),
    path('oquch/<int:pk>/', Oquch.as_view(), name='oquch'),
    path('category/<int:gradue_id>/', views.category, name="category")
]
