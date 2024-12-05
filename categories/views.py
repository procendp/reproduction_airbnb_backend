from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()






######################################################################
################ before refactoring with ViewSet #####################
######################################################################
# ### ------ before use django REST framework ------ 
# # from django.http import JsonResponse
# # from django.core import serializers

# class Categories(APIView):

#     def get(self, request):
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)      # all_categories : list  -->  many=True도 함께 
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)      # from user to serializer
        
#         if serializer.is_valid():
#             new_category = serializer.save()
#             return Response(CategorySerializer(new_category).data)
#         else:
#             return Response(serializer.errors)

# class CategoryDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise NotFound
#         return category

#     def get(self, request, pk):
#         serializer = CategorySerializer(self.get_object(pk))        # from django to Json
#         return Response(serializer.data)                            # 해당 데이터 응답으로 보내줌
    
#     def put(self, request, pk):
#         serializer = CategorySerializer(self.get_object(pk), data=request.data, partial=True)
#         if serializer.is_valid():
#             updated_category = serializer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.error)

#     def delete(self, request, pk):
#         self.get_object(pk).delete()
#         return Response(status= HTTP_204_NO_CONTENT)








# #########################################
# ##### original (before refactoring) #####
# #########################################
# """ @api_view(["GET", "POST"])
# def categories(request):

#     if request.method == "GET":
#         all_categories = Category.objects.all()
#         serializer = CategorySerializer(all_categories, many=True)      # all_categories : list  -->  many=True도 함께 
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = CategorySerializer(data=request.data)      # from user to serializer
        
#         if serializer.is_valid:
#             new_category = serializer.save()
#             return Response(CategorySerializer(new_category).data)
#         else:
#             return Response(serializer.errors)
    
#     ### ------ before use django REST framework ------ 
#     # all_categories = Category.objects.all()     # queryset
#     # return JsonResponse({'ok': True, 'categories': serializers.serialize("json", all_categories)})      # queryset을 Json으로 serialize

# @api_view(["GET", "PUT", "DELETE"])
# def category(request, pk):
#     try:
#         category = Category.objects.get(pk=pk)
#     except Category.DoesNotExist:
#         raise NotFound
    
#     if request.method == "GET":
#         serializer = CategorySerializer(category)       # from django to Json
#         return Response(serializer.data)                # 해당 데이터 응답으로 보내줌
#     elif request.method == "PUT":
#         serializer = CategorySerializer(category, data=request.data, partial=True)
#         if serializer.is_valid():
#             updated_category = serializer.save()
#             return Response(CategorySerializer(updated_category).data)
#         else:
#             return Response(serializer.error)
#     elif request.method == "DELETE":
#         category.delete()
#         return Response(status= HTTP_204_NO_CONTENT) """
