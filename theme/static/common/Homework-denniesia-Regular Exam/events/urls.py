from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.EventsView.as_view(), name='events'),
    path('create', views.EventCreateView.as_view(), name='event-create'),
    path('<int:event_pk>/', include([
        path('details/', views.EventDetailsView.as_view(), name='event-details'),
        path('edit/', views.EventEditView.as_view(), name='event-edit'),
        path('delete/', views.EventDeleteView.as_view(), name='event-delete'),
    ])
         )
]
