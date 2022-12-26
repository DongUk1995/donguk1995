from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class user_impo(APIView):
    def get(self, request):
        all_user = User.objects.all()
        serializer = UserSerializer(all_user, many=True)
        return Response(serializer.data)


class user_impose(APIView):
    def get_object(self, pk):
        try:
            return User.objects.all(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
