
from . import views
from django.urls import path


urlpatterns = [
    # home page
    path('', views.PostList.as_view(), name='posts'),
    # route for posts
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.home, name="home"),
]