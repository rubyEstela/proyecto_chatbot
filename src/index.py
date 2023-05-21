import http.client
import ssl 

conn = http.client.HTTPSConnection("api.ultramsg.com",context = ssl._create_unverified_context())

payload = "token=eax02ekg4er1oezk&to=+573145077586&body=WhatsApp API on UltraMsg.com works good"
payload = payload.encode('utf8').decode('iso-8859-1') 

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/instance47825/messages/chat", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))