"""
URL configuration for website project.

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
# Imports
from django.contrib import admin
from django.urls import path, include
from web import views
from django.conf import settings
from django.conf.urls.static import static

# Url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.aboutme, name="aboutme"),
    path('game/', views.game, name='game'),
    path('chainportal/', views.chainportal, name="chainportal"),
    path('Web3shop/', views.web3shop, name="web3shop"),
    path('MovieCatalog/', views.MovieCatalog, name="moviecatalog"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
# For Vercel
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# For handling 404 error
handler404 = 'web.views.handler404'
