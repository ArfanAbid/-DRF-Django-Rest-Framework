from django.http import JsonResponse  
import json

def api_home(request, *args,**kwargs):
    # request -> HttpRequest in django
    # print(dir(request))
    # request.body
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
    
    
    
    return JsonResponse(data)
    