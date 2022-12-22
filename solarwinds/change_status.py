from orionsdk import SwisClient
import urllib3

# Change status of IP in SolarWinds IPAM

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 1 = Used
# 2 = Available
# 4 = Reserved 

username = ""
password = ""
server = ""
ip_address = "x.x.x.x"

def change_status():
    swis = SwisClient(server, username, password, verify=False)
    results = swis.invoke(
        "IPAM.SubnetManagement",
        "ChangeIpStatus",
        ip_address,
        2 # Status Code
    )
    print(results)
    return results

change_status()
