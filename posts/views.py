from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import IsAuthorOrReadOnly
from .pagination import ListPagination
from django_filters import rest_framework as filterset
from rest_framework import filters
from rest_framework import viewsets


class PostViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = ListPagination


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializers
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = ListPagination

# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#     authentication_classes = (TokenAuthentication,)
#
#
# class PostListView(generics.ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     # permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#     pagination_class = ListPagination
#     filter_backends = (filterset.DjangoFilterBackend, filters.SearchFilter)
#     filterset_fields = ('author', 'title', 'created_at',)
#     search_fields = ('author', 'title', 'created_at',)


# class PostDelete(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
# class PostCreate(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
# class PostUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers


# class CommentList(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentListSerializers
#     pagination_class = ListPagination
#
#
# class CommentCreateView(generics.CreateAPIView):
#     serializer_class = CommentCreateSerializers
#     permission_classes = (permissions.IsAuthenticated, )
#     authentication_classes = (TokenAuthentication, )
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data = request.data)
#         post = Post.objects.get(pk=request.data['post'])
#
#         if post.author == self.request.user:
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             headers = self.get_success_headers(serializer.data)
#             return Response({'Comment created successfully'}, status=status.HTTP_201_CREATED, headers=headers)
#         else:
#             return Response({'You dont have permissions'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSelializers
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSelializers

class UserViewSets(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSelializers
