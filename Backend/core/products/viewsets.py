from rest_framework import viewsets,mixins
from . models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New  Instance
    put -> Update
    patch -> partial Update
    delete -> Destroy    
    '''
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk' # default

class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
    ):
    '''
    get -> list -> queryset
    get -> retrieve -> Product Instance Detail View  
    '''
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk' # default
