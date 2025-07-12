from django.urls import path, include
from . import views
urlpatterns = [
    path('overview/', views.EventsOverviewView.as_view(), name='events'),
    path('create/', views.EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/', include([
        path('', views.EventDetailsView.as_view(), name='event-details'),

        path('edit/', views.EventEditView.as_view(), name='event-edit'),
        path('delete/', views.EventDeleteView.as_view(), name='event-delete'),

    ])),
    path('my-events/', views.MyEventsView.as_view(), name='my-events'),
    path("api/", include("beaunity.event.api_urls")),
]