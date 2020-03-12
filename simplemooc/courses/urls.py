from django.urls import path
from simplemooc.courses import views

app_name='simplemooc'

urlpatterns = [	
	path('', views.index,name='index'),
]