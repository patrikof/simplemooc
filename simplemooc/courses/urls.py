from django.urls import path
from simplemooc.courses import views

urlpatterns = [	
	path('', views.courses,name='index'),
]