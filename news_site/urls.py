from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('back/', back, name='back'),
    path('feedback/', feedback, name='feedback'),
    path('add_news/', AddPost.as_view(), name='add_news'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
    path('category/<slug:cat_slug>/',   ShowCategory.as_view(), name='category'),
    path('comment/<int:pk>/', AddComment.as_view(), name='comment')
]
