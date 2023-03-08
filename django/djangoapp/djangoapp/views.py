from django.contrib.auth.models import User
from rest_framework import viewsets
from djangoapp.serializers import UserSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
