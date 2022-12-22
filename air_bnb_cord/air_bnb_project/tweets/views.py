from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from .serializers import TweetSerializer
from .models import Tweet


@api_view(["GET", "POST"])
def tweeters(request):
    if request.method == "GET":
        all_tweeters = Tweet.objects.all()
        serializer = TweetSerializer(all_tweeters, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            new_tweet = serializer.save(user=request.user)
            return Response(
                TweetSerializer(new_tweet).data,
            )
        else:
            Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def tweeter(request, pk):
    try:
        tweeter = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        serializer = TweetSerializer(tweeter)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TweetSerializer(
            tweeter,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_tweeter = serializer.save()
            return Response(TweetSerializer(updated_tweeter).data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        tweeter.delete()
        return Response(status=HTTP_204_NO_CONTENT)
