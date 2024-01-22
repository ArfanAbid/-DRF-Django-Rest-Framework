import requests

# endpoint="https://httpbin.org/anything"
# endpoint="http://localhost:8000/" #http://127.0.0.1:8000/
endpoint="http://localhost:8000/api/" #http://127.0.0.1:8000/





get_response=requests.get(endpoint,params={"abc":123},json={"query":"Hello World!"}) # HTTP request
# print(get_response.text) #print raw text response
# print(get_response.status_code) #print status code response
print(get_response.json()) #print json response





# HTTP request -> HTMLls
# REST API HTTP request -> JSON
# JSON JavaScript Object Notation  ~ python dictionary
