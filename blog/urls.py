from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, published_toggle, view_all

app_name = BlogConfig.name

# урлы приложения blog
urlpatterns = [
    path('create', PostCreateView.as_view(), name='create'),
    path('', PostListView.as_view(), name='list'),
    path('view_all', view_all, name='view_all'),
    path('view/<int:pk>', PostDetailView.as_view(), name='view'),
    path('edit/<int:pk>', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('published/<int:pk>', published_toggle, name='published_toggle'),
]
