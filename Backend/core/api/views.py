from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer




#from django.http import JsonResponse,HttpResponse 
#def api_home(request, *args,**kwargs):
    # request -> HttpRequest in django
    # print(dir(request))
    # request.body
'''
    print(request.GET) # url query params
    body = request.body  # Gives byte string of JSON data 
    data={}
    try:
        data = json.loads(body) # String of JSON data -> python Dict  
    except:
        pass    
    print(data)
    # data['headers'] = request.headers # request.META  -> should be in python dict 
    data['params'] =dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] =request.content_type
    '''

    
    #model_data=Product.objects.all().order_by("?").first()
    #data={}
    #if model_data:
'''data['id']=model_data.id
        data['title']=model_data.title
        data['content']=model_data.content
        data['price']=model_data.price
        # model instance (model_data)
        # turn a python dict
        # return JSON to my client'''

        #data=model_to_dict(model_data,fields=['id','title','price'])
        #return JsonResponse(data)
'''data=dict(data)
        json_data_str=json.dumps(data)


    return HttpResponse(json_data_str,headers={"content-type": "application/json"})'''

@api_view(["GET"])
def api_home(request, *args,**kwargs):
                # DRF API view
    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:
        #data=model_to_dict(instance,fields=['id','title','price'])
        data=ProductSerializer(instance).data
        return Response(data)

