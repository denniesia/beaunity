from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', include([
        path('edit/', views.CommentEditView.as_view(), name='comment-edit'),
    ]))
]
