from django.urls import include, path

from . import views


urlpatterns = [
    path("<int:pk>/", include([
        path("edit/", views.CommentEditView.as_view(), name="comment-edit"),
        path("delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
        ]),
    )
]
