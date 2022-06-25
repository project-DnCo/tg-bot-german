from django.urls import path

from . import views


app_name = 'words'

urlpatterns = [
    path('random/', views.RandomWordAPIView.as_view(), name='random'),
    path('next/<int:pk>/', views.NextWordAPIView.as_view(), name='next'),
]
