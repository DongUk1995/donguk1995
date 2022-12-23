from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from .serializers import TweetSerializer
from .models import Tweet


class tweeters(APIView):
    def get(self, request):
        all_tweeters = Tweet.objects.all()
        serializer = TweetSerializer(all_tweeters, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            new_tweet = serializer.save(user=request.user)
            return Response(TweetSerializer(new_tweet).data)
        else:
            Response(serializer.errors)


class tweeter(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.all(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(
            tweet,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(TweetSerializer(updated_tweet).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)
