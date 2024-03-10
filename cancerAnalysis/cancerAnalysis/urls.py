from django.contrib import admin
from django.urls import path
from cancerAnalysis import views  # Make sure to replace 'myapp' with the actual name of your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.client_side_landing, name='clientside_landing'),
    path('virtual-staining.html', views.virtual_staining, name='virtual_staining'),
    path('spatial-features.html', views.spatial_features, name='spatial_features'),
]
