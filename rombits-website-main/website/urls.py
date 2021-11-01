from django.urls import path
from website import views
from . import views


urlpatterns = [
    path('', views.index),  #the path for our index view
    path('user_login/', views.user_login, name='user_login'),
    path('cloud/',views.cloud,name='cloud'),
    path('security/',views.security,name='security'),
    path('business_solution/',views.business_solution,name='business_solution'),
    path('ai_hub/',views.ai_hub,name='ai_hub'),
    path('consulting/',views.consulting,name='consulting'),

]
