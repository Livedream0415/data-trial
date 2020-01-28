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
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        index = int(self.request.GET.get("index", self.queryset.count()-1))
        vector = int(self.request.GET.get("vector", -10))
        sort = self.request.GET.get("sort", "username")

        if vector < 0:
            vector = -vector
            index = index - vector + 1
        if index < 0:
            vector += index
            index = 0
        if sort == "username":
            sort = "-username"

        user_list = self.queryset.order_by(sort)[index:index+vector]
        serialized_user_list = UserSerializer(user_list, many=True)
        return JsonResponse({
            "total_length": self.queryset.count(),
            "array": serialized_user_list.data
        })

    def create(self, request):
        is_existed = User.objects.filter(
            username=request.data['username']
        ).count()
        if is_existed == 0:
            user = UserSerializer(data=request.data)
            user.timestamp = parse_datetime(request.data['timestamp'])
            if user.is_valid():
                user.save()
            return JsonResponse({'id': user.data['id']}, status=200)
        else:
            return JsonResponse({
                'error': 'username is already in use'
            }, status=409)


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request):
        index = int(self.request.GET.get("index", self.queryset.count()-1))
        vector = int(self.request.GET.get("vector", -10))

        if vector < 0:
            vector = -vector
            index = index - vector + 1
        if index < 0:
            vector += index
            index = 0

        message_list = self.queryset[index:index+vector]
        serialized_message_list = MessageSerializer(message_list, many=True)
        return JsonResponse({
            "total_length": self.queryset.count(),
            "array": serialized_message_list.data
        })

    def create(self, request):
        message = MessageSerializer(data=request.data)
        message.timestamp = parse_datetime(request.data['timestamp'])
        if message.is_valid():
            message.save()
        return JsonResponse({"id": message.data["id"]})
