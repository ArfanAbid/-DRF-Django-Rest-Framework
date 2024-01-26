import requests

endpoint="http://localhost:8000/api/products/" 
headers={'Authorization': 'Bearer dc3074ad161dbe4128977f6c92a6e89660e8275a'}
data={
    "title":"THis field is done",
    "content":"DRF related content"
}

get_response=requests.post(endpoint,json=data,headers=headers) # HTTP request
print(get_response.json()) #print json response

