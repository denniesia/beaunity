"""
URL configuration for beaunity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("beaunity.common.urls")),
    path("accounts/", include("beaunity.accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path("category/", include("beaunity.category.urls")),
    path("post/", include("beaunity.post.urls")),
    path("comment/", include("beaunity.comment.urls")),
    path("event/", include("beaunity.event.urls")),
    path("challenge/", include("beaunity.challenge.urls")),
    path("interaction/", include("beaunity.interaction.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

