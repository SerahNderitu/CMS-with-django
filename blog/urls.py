
from . import views
from django.urls import path
from .views import contact


urlpatterns = [
    # home page
    path('', views.PostList.as_view(), name='posts'),
    path('contact/', contact, name='contact'),

    # route for posts
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.home, name="home"),
]
