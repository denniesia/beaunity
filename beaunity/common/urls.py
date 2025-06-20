from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

]
handler403 = custom_permission_denied_view