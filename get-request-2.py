import urllib3
http = urllib3.PoolManager()

resp = http.request('GET', 'http://tutorialspoint.com/robots.txt')
print(resp.data)

# get the status of the response
print(resp.status)