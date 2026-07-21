
# from django.contrib import admin
# from django.urls import path , include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", include('sekou.urls')), 
#     path('', include('DepensesMensuel.urls')),  # On inclut les URLs de notre app
    
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DepensesMensuel.urls')),
]

