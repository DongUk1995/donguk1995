from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer  # 번역기를 만들었다.


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        Category.objects.create(
            name=request.data["name"],
            kind=request.data["kind"],
        )
        return Response({"created": True})


@api_view()
def category(request, pk):  ## url로 부터 호출된 모든 view들은 request 객체를 받는다.
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)
