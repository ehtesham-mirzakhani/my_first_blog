from django.urls import path
from . import views
urlpatterns = [
    path('',views.post_list ),
    path('show',views.show ),
    path('post5',views.post5 ),
    path('post/<int:pks>/', views.post_detail, name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pks>/edit/', views.post_edit, name='post_edit'),
]
