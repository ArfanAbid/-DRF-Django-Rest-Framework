from rest_framework import serializers
from rest_framework.reverse import reverse

from  .models import Product
from  . import validators

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url= serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    title=serializers.CharField(validators.validate_title_no_hello,validators.unique_product_title)
    email=serializers.EmailField(wite_only=True)
    class Meta:
        model=Product
        fields=('url','edit_url','email','pk','title','content','price','sale_price','my_discount',)

    def validate_title(self, value):
        request=self.context.get('request') 
        user=request.user
        qs=Product.objects.filter(uaer=user,title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError({"title": "This title is already taken"})
        return value
    # def create(self,validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email=validated_data.pop('email')
    #     obj=super().create(validated_data)
    #     return obj 
    
    # def update(self,instance,validated_data):
    #     # email=validated_data.pop('email')
    #     return super().update(instance,validated_data)
        
    def get_edit_url(self,obj):
        # return f"/api/v2/products/{obj.pk}/"
        request=self.context.get('request')  # self.request
        if request is None: return None

        return reverse("product-edit",kwargs={'pk':obj.pk},request=request)

    def get_my_discount(self,obj):
        if not hasattr(obj, 'id'): # or if not isinstance(obj,'id):
            return None
        return obj.get_discount()    
    