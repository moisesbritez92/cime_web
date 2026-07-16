"""URL configuration for cime_project.

The landing site lives at the root. As the platform grows into a full
back-office system, mount new apps here (e.g. path('clientes/', ...)).
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
]

# Serve uploaded media during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
