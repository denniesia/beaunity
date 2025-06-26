from django.urls import path
from . import views
urlpatterns = [
    path('like/<str:model_name>/<int:object_id>/', views.like_functionality, name='like' ),

]