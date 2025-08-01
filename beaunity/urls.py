from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from beaunity.common.views import custom_permission_denied_view
urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("beaunity.main.urls")),
    path("common/", include("beaunity.common.urls")),
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

handler403 = 'common.views.custom_permission_denied_view'
