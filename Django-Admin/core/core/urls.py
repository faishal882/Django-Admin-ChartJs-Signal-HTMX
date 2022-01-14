from django.contrib import admin
from django.urls import path, include
from blog.admin import blog_site
from bookstore.admin import bookstore_site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
    path('bookstoreadmin/', bookstore_site.urls),
    path('summernote/', include('django_summernote.urls')),
]
# ] + static(settings.STATIC_URL,
# document_root = settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


# admin.site.index_title = "The Bookstore"
# admin.site.site_header = "The Bookstore Admin"
# admin.site.site_title = "Site Title Bookstore"
