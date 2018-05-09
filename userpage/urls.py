from django.conf.urls import url
from django.contrib.auth import views as auth_views
import views
app_name = "userpage"

urlpatterns = [

    url(r'^register/',views.register,name = "register"),
    url(r'^login/', views.loginUser, name="login"),
    url(r'^logout/', views.logoutUser, name="logout"),
    url(r'^cpanel/', views.cpanel, name="cpanel"),


]