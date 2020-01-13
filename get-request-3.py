import urllib3
http = urllib3.PoolManager()

resp = http.request('GET', 'http://34.94.72.188/v1/models/bkash_banner:predict')
print(resp.data)

# get the status of the response
print(resp.status)