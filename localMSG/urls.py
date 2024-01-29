from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from mymessages.views import index, update_messages, SignUp, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('update_messages/', update_messages, name='update_messages'),
    path(
        'signup/',
        SignUp.as_view(),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='login.html',
                          redirect_authenticated_user=True),
        name='login'
    ),
    path(
        'logout/',
        logout_view,
        name='logout'
    ),
    path('admin/', admin.site.urls),
]
