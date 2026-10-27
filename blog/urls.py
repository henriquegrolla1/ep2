from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='create'),
    path('posts/update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('posts/delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('posts/<int:post_id>/comment/', views.create_comment, name='comment'),
]
