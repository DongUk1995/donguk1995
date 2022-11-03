from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer  # 번역기를 만들었다.


@api_view()
def categories(requeset):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories, many=True)
    return Response(
        {
            "ok": True,
            "categories": serializer.data,
        }
    )
