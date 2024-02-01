from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from . models import Product


# def validate_title( value):
#         qs=Product.objects.filter(title__iexact=value)
#         if qs.exists():
#             raise serializers.ValidationError({"title": "This title is already taken"})
#         return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError({"title": "This title is already taken"})
    return value 

unique_product_title=UniqueValidator(queryset=Product.objects.all())