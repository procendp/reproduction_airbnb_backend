from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
# from .serializers import CategorySerializer       # 왜 이거지?
from .serializer import CategorySerializer

### ------ before use django REST framework ------ 
# from django.http import JsonResponse
# from django.core import serializers

# Create your views here.

@api_view(["GET", "POST"])
def categories(request):

    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)      # all_categories : list  -->  many=True도 함께 
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)      # from user to serializer
        
        if serializer.is_valid:
            return Response({'created': True})
        else:
            return Response(serializer.errors)
    
    ### ------ before use django REST framework ------ 
    # all_categories = Category.objects.all()     # queryset
    # return JsonResponse({'ok': True, 'categories': serializers.serialize("json", all_categories)})      # queryset을 Json으로 serialize

@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)       # from django to Json
    return Response(serializer.data)