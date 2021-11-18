from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.blogpost, name='blogpost'),
    path('<int:post_id>/edit', views.postedit, name='postedit'),
    path('<int:post_id>/change', views.changepost, name='changepost'),
    path('<int:post_id>/delete', views.deletepost, name='deletepost'),
    path('add', views.add, name='add'),
    path('addpost', views.addpost, name='addpost'),
]
