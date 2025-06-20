from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

]
handler403 = views.custom_permission_denied_view