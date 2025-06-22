from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.OrganizerCreateView.as_view(), name='organizer-create'),
    path('details/', views.OrganizerDetailsView.as_view(), name='organizer-details'),
    path('edit/', views.OrganizerEditView.as_view(), name='organizer-edit'),
    path('delete/', views.OrganizerDeleteView.as_view(), name='organizer-delete'),
]
