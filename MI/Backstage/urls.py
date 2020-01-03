
from django.urls import path,re_path
from Backstage.views import *
urlpatterns = [
    path('register/',register),
    path("login/",login),
    path("index/",index),
    path("add_comm/",add_comm),
    path("logout/",logout),
    path("self_info/",self_info),
    path("edit_self_info/",edit_self_info),
    path("forget_password/",forget_password),
    path("change_password/",change_password),
    path("comm_list/",comm_list),
    path("add/",add),
]