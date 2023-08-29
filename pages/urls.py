from django.urls import path
from .views import HomePageView, AboutPageView, DeletePageView, BonusStagePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("delete/", DeletePageView.as_view(), name="delete"),
    path("edit/", DeletePageView.as_view(), name="edit"),
    path('bonus/', BonusStagePageView.as_view(), name='bonus'),
]