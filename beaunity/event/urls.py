from django.urls import path
from . import views
urlpatterns = [
    path('', views.EventsOverviewView.as_view(), name='events'),
]