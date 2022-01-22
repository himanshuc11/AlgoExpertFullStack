from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rce/', include('rce.urls')),
    path('auth/', include('problems.urls')),
    path('problems/', include('problems.urls')),
    path('payment/', include('payment.urls')),
]
