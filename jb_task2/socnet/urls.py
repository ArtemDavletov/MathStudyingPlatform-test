from django.urls import path
from .views import UsersListView, UserView, UserCreateView, RelationshipView, RelationshipsListView, \
    DeleteRelationshipView

app_name = "users"


urlpatterns = [
    path('all_users/', UsersListView.as_view()),
    path('user/', UserCreateView.as_view()),
    path('relationship/', RelationshipView.as_view()),
    path('relationship/<str:user_login>&<str:friend_login>', DeleteRelationshipView.as_view()),
    path('all_relationships/', RelationshipsListView.as_view()),
    path('user/<str:login>', UserView.as_view())
]
