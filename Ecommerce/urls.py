
from django.contrib import admin
from django.urls import path, include
from .import settings
from django.conf.urls.static import static

urlpatterns = [
    path('customAdmin/', include('customAdmin.urls')),
    path('dj-admin/', admin.site.urls),
    path('',include('store.urls')),
    path('cart/',include('cart.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

    
    
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



  