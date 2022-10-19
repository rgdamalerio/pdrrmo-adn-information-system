"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

## Set this if using django rest framework
# from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from rest_framework.routers import DefaultRouter
# from users.views import UserViewSet

admin.site.index_title = "PDRRMO-ADN"
admin.site.site_title = "PDRRMO Agusan-Norte Admin Portal"
admin.site.site_header = "PDRRMO-ADN Information System"

urlpatterns = [
    # Redirect home view to admin:index
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path("admin/", admin.site.urls),
    path('',include('household.urls')),
    path('address/',include('library.urls')),
    path('aggregate/',include("aggregate.urls")),
    #path('reports/',include('reports.urls')),
    ## URL for api rest framework
    #path('api-auth/', include('rest_framework.urls')),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#router = DefaultRouter()
#router.register('user',UserViewSet,basename='user')

#urlpatterns += router.urls
