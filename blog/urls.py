from django.urls import path
from .views import (
    BlogDetailView,
    BlogListView,
    CategoryListView,
)


urlpatterns = [
    path("<str:category>/", CategoryListView.as_view(), name="category"),
    path("", BlogListView.as_view(), name="home"),
    path("<str:slug>/", BlogDetailView.as_view(), name="detail"),
    # path("education/", EducationListView.as_view(), name="education"),
    # path("politics/", PoliticsListView.as_view(), name="politics"),
    # path("food/", FoodListView.as_view(), name="food"),
    # path("motivation/", MotivationListView.as_view(), name="motivation"),
]
