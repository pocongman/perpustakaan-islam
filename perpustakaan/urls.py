from django.contrib import admin
from django.urls import path, include

#Media
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('buku.urls')),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('books/', books, name='books'),
    
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)