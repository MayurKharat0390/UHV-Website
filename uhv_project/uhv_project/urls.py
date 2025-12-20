from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('users/', include('users.urls')),
    path('reflections/', include('reflections.urls')),
    path('journals/', include('journals.urls')),
    path('activities/', include('activities.urls')),
    path('voices/', include('voices.urls')),
    path('faculty/', include('faculty.urls')),
    path('resources/', include('resources.urls')),
    path('progress/', include('progress.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
