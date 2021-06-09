from django.contrib import admin
from django.urls import path
from views import scitc_login
from views import user
from model import schedule

urlpatterns = [
    path('', scitc_login.mylogin),
    path('user/', user.user_info,name='user'),
    path('user/user_update', user.user_update),
    path('logout/',user.user_logout,name='logout'),
    path('admin/', admin.site.urls),
]
