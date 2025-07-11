from django.urls import path

from . import views

urlpatterns = [
    path("like/<str:model_name>/<int:object_id>/", views.like_functionality, name="like"),
    path("favourite/<str:model_name>/<int:object_id>/", views.favourite_functionality, name="favourite"),
    path("join/<str:model_name>/<int:pk>/", views.join_functionality, name="join-functionality"),
]
