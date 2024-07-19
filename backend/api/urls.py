from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (

    TokenRefreshView,
)
urlpatterns =[
    path('', views.getRoutes),
    path('posts/',views.getAllPosts,name="posts"),
    path('create/',views.createPost,name="create"),
    path('update/<str:pk>/',views.updatePost,name="update"),
    path('delete/<str:ck>/',views.deletePost,name="delete"),
    path('register/',views.registeration_view,name="register"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



