from django.urls import path
from . import views

app_name = 'bbs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/', views.detail, name='detail'),

    path('form_page', views.form_page, name="form_page"),
]
