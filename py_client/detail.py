import requests

endpoint="http://localhost:8000/api/products/10" 

get_response=requests.get(endpoint) # HTTP request
print(get_response.json()) #print json response

