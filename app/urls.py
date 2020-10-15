from django.urls import path
from app.views import *
urlpatterns = [
    path('main_page', index),
    path('ma',login_user),
    path('pa',register),
    path('ka',do_logout),
    path('main_page1', index1),
    path('main_page2',index2),
    path('ajax_path', ajax_path)



]