from django.urls import path
from .views import BlogListView, detail_view


urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("<str:slug>/", detail_view, name="detail"),
]
