from django.urls import path

from .views import (

    sign_up,

    login_request,

    logout_request,
)


app_name = 'custom_users'


urlpatterns = [

    path('signup/', sign_up, name='signup'),

    path('login/', login_request, name='login'),

    path('logout/', logout_request, name='logout'),

]


