from django.urls import include, path
from .views import PostCreate, PostList, PostDetail, PostUpdate, PostDelete


# urlpatterns = [
#     path("", views.index, name="index"),
# ]



urlpatterns = [
    path('create/', PostCreate.as_view(), name='create-post'),
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view(), name='retrieve-post'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='update-post'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='delete-post')
]