import requests

endpoint="http://localhost:8000/api/products/1/update/" 

data= {
    "title":"new title",
    "content":"new content",
    "price":128.22
}

get_response=requests.put(endpoint,json=data) # HTTP request
print(get_response.json()) #print json response

