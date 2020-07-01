from django.urls import path
from learn_users import views

app_name = 'learn_users'
urlpatterns = [
    path('index/',views.index, name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="user_login"),
]
