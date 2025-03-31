from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path('get/', views.BlogPostList.as_view(), name='blogpost-view'),
    path('delete/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-view-update')
]