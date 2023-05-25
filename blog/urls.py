from django.urls import path
from . import views
urlpatterns = [
    path('',views.post_list ),
    path('show',views.show ),
    path('post5',views.post5 ),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
