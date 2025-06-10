
from django.urls import path
from .views import CategoryOverviewView

urlpatterns = [
    path('', CategoryOverviewView.as_view(), name='category-overview'),


]
