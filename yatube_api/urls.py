from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('posts/(?P<post_id>[^/.]+)/comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
