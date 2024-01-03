
from django.urls import path
from api.views import UserProfileCreateView

urlpatterns = [
    path('user-create/', UserProfileCreateView.as_view(), name='user-create'),
]
