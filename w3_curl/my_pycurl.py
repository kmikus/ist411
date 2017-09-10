import pycurl
from io import BytesIO

buffer = BytesIO()
url = "http://pycurl.io/"

curlHandle = pycurl.Curl()
curlHandle.setopt(curlHandle.URL, url)
curlHandle.setopt(curlHandle.WRITEDATA, buffer)
curlHandle.perform()
curlHandle.close()

body = buffer.getvalue().decode("UTF-8")
print(body)

