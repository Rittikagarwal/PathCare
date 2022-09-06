from django.urls import path
from . import views
urlpatterns=[
path('login', views.login),
path('success',views.success),
path('signup',views.signup),
path('db_update', views.db_update),






]