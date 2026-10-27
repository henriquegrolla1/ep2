from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.list_posts, name='index'),
    path('posts/<int:post_id>/', views.detail_post, name='detail'),
    path('posts/create/', views.create_post, name='create'),
    path('posts/update/<int:post_id>/', views.update_post, name='update'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete'),
]
