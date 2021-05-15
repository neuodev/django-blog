from django.urls import path

from .views import PostList, PostDetail, UserList, UserDetails

urlpatterns = [
    path('<int:pk>', PostDetail.as_view()),
    path('',PostList.as_view()), 
    path('users/', UserList.as_view()),
    path('users?<int:pk>', UserDetails.as_view()),
]