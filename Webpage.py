import http.client

Connection = http.client.HTTPSConnection("www.indiandataclub.com")
Connection.request("GET", "/")
response = Connection.getresponse()
data = response.read()

with open("IDC.html", "w", encoding="utf-8") as f:
    f.write(data.decode())


print(" Webpage saved as 'idc.html'")
Connection.close()
