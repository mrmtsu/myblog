from django.urls import path

from . import views
from .views import IndexView, PostDetailView, CategoryListView, TagListView, CategoryPostView, TagPostView

app_name = 'myblog'

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('contact/', views.contact, name='contact'),
  path('contact/complete/', views.complete, name='complete'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
  path('categories/', CategoryListView.as_view(), name='category_list'),
  path('tags/', TagListView.as_view(), name='tag_list'),
  path('category/<str:category_slug>/',CategoryPostView.as_view(), name='category_post'),
  path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
]