from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json, yaml
#===========================================================================================================
def ProcessYAML (yaml_file) :
    '''This function opens the yaml file and returns the data object'''
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (y_data)  
#===========================================================================================================
def jprint(obj):                                            # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=8)
    print(text)
#===========================================================================================================
yaml_data = ProcessYAML('certs.yaml')                                     #yaml settings are global variables
debug = yaml_data['debug']                                                #debug mode?
#===========================================================================================================
#some site without http/https in the path
base_url = 'myfootprint.co.nz'
port = '443'

ssls = yaml_data['ssls']

for host_name in ssls :  
    print(f"Checking {host_name}")
    #hostname = base_url
    context = ssl.create_default_context()

    with socket.create_connection((host_name, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host_name) as ssock:
            #print(ssock.version())
            cert=ssock.getpeercert()
            #data = json.dumps(cert)
            #print(ssock.getpeercert())
            for key in cert:
                print(key, ' : ', cert[key])

#print("\n", cert['subject'])
#print(cert['issuer'])
#print(cert['version'])
#print(cert['notBefore'])
#print(cert['notAfter'])
#print(cert)

