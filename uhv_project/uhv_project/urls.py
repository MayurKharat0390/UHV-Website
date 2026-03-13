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
    path('innovations/', include('innovations.urls')),
]

# Universal serving of static and media files for Vercel/Serverless
from django.views.static import serve
from django.urls import re_path

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
