from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('login/', views.login_view, name='login'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update_location/', views.update_location, name='update_location'),
    path('save_marker/', views.save_marker, name='save_marker'),
    path('load_markers/', views.load_markers, name='load_markers'),
]

