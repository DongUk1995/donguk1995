from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import TweetSerializer
from .models import Tweet


class Tweet_main(APIView):
    def get(self, request):
        all_Tweet_main = Tweet.objects.all()
        serializer = TweetSerializer(all_Tweet_main, many=True)
        return Response(serializer.data)
