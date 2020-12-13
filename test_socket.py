from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json

def jprint(obj):                                            # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=8)
    print(text)

#some site without http/https in the path
base_url = 'myfootprint.co.nz'
port = '443'

hostname = base_url
context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        cert=ssock.getpeercert()
        #data = json.dumps(cert)
        #print(ssock.getpeercert())

#print("\n", cert['subject'])
#print(cert['issuer'])
#print(cert['version'])
#print(cert['notBefore'])
#print(cert['notAfter'])
#print(cert)

for key in cert:
    print(key, ' : ', cert[key])