import http.client

conn = http.client.HTTPSConnection("www.indiandataclub.com")
conn.request("GET", "/")
response = conn.getresponse()
data = response.read()

with open("IDC.html", "w", encoding="utf-8") as f:
    f.write(data.decode())


print(" Webpage saved as 'idc.html'")
conn.close()
