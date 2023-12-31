"""
URL configuration for localife_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path , include
from home_app import views
from django.conf import settings 
from django.conf.urls.static import static 
#from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home_app, name="home_app"),
    path("home/",include('home_app.urls')),
    path("user/",include('user_app.urls')),
    path("search/",include('search_app.urls')),    
    path("post/",include('post_app.urls')),
    path("book/",include('match_app.urls')),
    path("finished/",include('finished_app.urls')),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="schema_docs"), 
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT) 

