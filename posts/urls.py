from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter()
router.register('users', UserViewSets, basename='users')
router.register('comment', CommentViewSets, basename='comment')
router.register('', PostViewSets, basename='post')


urlpatterns = router.urls
# urlpatterns = [

    # path('users/', UserList.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()),

    # path('', PostListView.as_view(), name='list'),
    # path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    # path('comment/', CommentList.as_view(), name='comment_list'),
    # path('comment/create/', CommentCreateView.as_view(), name='comment_create'),
    # path('create/', PostCreate.as_view(), name='create'),
    # path('<int:pk>/update/', PostUpdate.as_view(), name='update'),
    # path('<int:pk>/delete/', PostDelete.as_view(), name='delete'),
# ]