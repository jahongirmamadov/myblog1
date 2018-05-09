from django.conf.urls import url
import views
app_name = "blog"

urlpatterns = [

    url(r'^$',views.home, name="blog"),
    url(r"^add",views.add, name ="add"),
    url(r"^articles", views.articles, name="articles"),
    url(r"^article/([0-9]+)/$", views.detail, name="detail"),
    url(r"^update/([0-9]+)/$", views.update, name="update"),
    url(r"^delete/([0-9]+)/$", views.delete, name="delete"),
    url(r"^comment/([0-9]+)/$", views.comment, name="comment"),
    url(r'^homepage', views.homepage,name="homepage"),

]