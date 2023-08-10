from django.urls import path
from . import views

app_name = "app_1"

urlpatterns = [
    path("", views.HomepageView.as_view(), name="home"),
    path("about/", views.AboutUsView.as_view(), name="about_page"),
]
