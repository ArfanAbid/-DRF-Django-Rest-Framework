import requests

endpoint="http://localhost:8000/api/products/" 
data={
    "title":"THis field is done",
    "content":"DRF related content"
}

get_response=requests.post(endpoint,json=data) # HTTP request
print(get_response.json()) #print json response

