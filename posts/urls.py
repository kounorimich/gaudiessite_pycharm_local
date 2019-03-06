from django.urls import path
from . import views
app_name = 'posts'
urlpatterns = [path('', views.PostPageIndex.as_view(), name='index'),]
               # path("<int:post_pk>", views.PostDetail.as_view(), name="post_detail"),]
