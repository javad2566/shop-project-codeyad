from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", include("home.urls")),
                  path('products/', include("product.urls")),
                  path('acounts/', include("accounts.urls")),
                  path("cart/", include("cart.urls")),
                  path("about/", include("about.urls"))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
