from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='music'),
    path('all_data', views.all_data, name='all_data')
]