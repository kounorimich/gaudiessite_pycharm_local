"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.conf import settings
from lives import views as lives_views


urlpatterns = [
    path('admin/', admin.site.urls),  # 管理者サイトの名前は、デフォルトで'admin:index'になっている
    path('top/', include('top.urls')),
    path('posts/', include('posts.urls')),
    path('lives/', lives_views.index, name='lives_index'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    #path(r'^$', RedirectView.as_view(url='/index/'), name='redirect_to_index'),
    #url(r'^$', RedirectView.as_view(url='/index/'), name='redirect_to_index')

urlpatterns += [re_path(r'\w*',  RedirectView.as_view(url='/top/'), name='redirect_to_index')]




if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
