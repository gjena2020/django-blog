from django.urls import path

from .views import BlogCreateView, BlogUpdationView, BlogListView, BlogDetailView, BlogDeleteView
app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdationView.as_view(), name='update'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),

]