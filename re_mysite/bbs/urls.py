from django.urls import path
from . import views

app_name = 'bbs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/', views.detail, name='detail'),

    path('page', views.page, name="page")
]
