from .serializers import MessageSerializer, UserSerializer
from api.models import User, Message
from rest_framework import viewsets
from django.utils.dateparse import parse_datetime
from django.http import JsonResponse
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        user = UserSerializer(data=request.data)
        user.timestamp = parse_datetime(request.data['timestamp'])
        if user.is_valid():
            user.save()
        return JsonResponse({"id": user.data["id"]})


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        message = MessageSerializer(data=request.data)
        message.timestamp = parse_datetime(request.data['timestamp'])
        if message.is_valid():
            message.save()
        return JsonResponse({"id": message.data["id"]})
