from django.urls import path, include
from . import views
urlpatterns = [
    path('overview/', views.EventsOverviewView.as_view(), name='events'),
    path('<int:pk>/', include([
        path('', views.EventDetailsView.as_view(), name='event-details'),
    ])),
]