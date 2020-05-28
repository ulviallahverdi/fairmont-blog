"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from user.views import signup,index,logoff,user_login,activate_account,upload_video
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from video.views import videos,video_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',signup,name="register"),
    url('^$',index,name="home"),
    path('logout/',logoff,name="logout"),
    path("login/",user_login,name="login"),
    path('activate/<str:id>',activate_account,name="activate"),
    path('video_upload',upload_video,name="upload_video"),
    path('shared_media',videos,name="shared_media"),
    path('view/<int:id>',video_detail,name="video_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
