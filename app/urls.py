from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('main_page', index),
    path('ma',login_user),
    path('pa',register),
    path('ka',do_logout),
    path('main_page1', index1),
    path('main_page2',index2),
    path('ajax_path', ajax_path),
    path('main_page3',index3),
    path('main_page4',index4),
    path('main_page5',index5),
    path('main_page6',index6)
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)