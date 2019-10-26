from django.urls import path
from . import views
app_name = 'case001'

urlpatterns = [
    path('a1/', views.a1, name='a1'),
    path('b1/<int:yr>/<int:mo>/', views.b1, name='b1'),
    path('b1/', views.b1_list, name='b1_list'),
    path('a2/', views.a2, name='a2'),
    path('a3/', views.a3, name='a3'),
    
    path('a1v2/', views.a1v2, name='a1v2'),
    path('a2v2/', views.a2v2, name='a2v2'),
    path('a3v2/', views.a3v2, name='a3v2'),
    path('a4v2/', views.a4v2, name='a4v2'),
    
    path('a8/', views.a8, name='a8'),
    # path('init_ww/', views.init_ww, name='init_ww'),
    # path('ww2/', views.ww2, name='ww2'),
    
    path('', views.index, name='index'),
]