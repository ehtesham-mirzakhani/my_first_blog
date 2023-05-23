from django.urls import path
from . import views
urlpatterns = [
    path('',views.post_list ),
    path('show',views.show ),
]
