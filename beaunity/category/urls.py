
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.CategoryOverviewView.as_view(), name='category-overview'),
    path('create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('<slug:category_slug>/', include([
         path('delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
         path('edit/', views.CategoryEditView.as_view(), name='category-edit'),
         path('details/', views.CategoryDetailsView.as_view(), name='category-details'),
    ])),


]
