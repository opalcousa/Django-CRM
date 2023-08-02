from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('stock/', include('stock.urls')),
    path('formulas/', include('formulas.urls')),
    path('accounting/', include('accounting.urls')),
]
