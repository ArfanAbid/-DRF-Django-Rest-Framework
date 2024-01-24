from rest_framework  import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from.serializers import ProductSerializer




class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductListAPIView(generics.RetrieveAPIView):
    ''' Actually not using this class'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(["GET", "POST"])
def product_alt_view(request,pk=None ,*args,**kwargs):
    method =request.method

    if method == "GET":
        if pk is not None:
        # Get request as detail view 
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
        # or list list view
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)

    if method== "POST":
        # Create an item
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        else:
            return Response({"invalid":"not good data"},status=400)
        


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_delete(self, instance):
        #instance
        super().perform_delete(instance)
