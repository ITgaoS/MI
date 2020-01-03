from django.urls import path,include
from Blient import views
urlpatterns = [
path('login/',views.login)
]