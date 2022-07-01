from requests.exceptions import ConnectionError
import requests
import json
import urllib3


urllib3.disable_warnings()

class GetDeviceData:
    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.headers = {
            "Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json"
        }
     

    def get_interface_config(self):
        """
        Get configuration from all interfaces.
        """
        url = f"https://{self.host}:{self.port}/restconf/data/ietf-interfaces:interfaces"
        try: 
            response = requests.get(
                url=url,
                headers=self.headers,
                auth=(self.username, self.password),
                verify=False
            )
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Failed - Status Code: {response.status_code}")
                return f"Failed - Status Code: {response.status_code}"
        except ConnectionError as e:
            print(f"{'*' * 50}\nJob Failed!\nError: {e}\n{'*' * 50}")
            return  f"{'*' * 50}\nJob Failed!\nError: {e}\n{'*' * 50}"

    def get_interface_stats(self):
        """
        Get interface statistics from all interfaces.
        """
        url = f"https://{self.host}:{self.port}/restconf/data/ietf-interfaces:interfaces-state"
        try: 
            response = requests.get(
                url=url,
                headers=self.headers,
                auth=(self.username, self.password),
                verify=False
            )
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Failed - Status Code: {response.status_code}")
                return f"Failed - Status Code: {response.status_code}"
        except ConnectionError as e:
            print(f"{'*' * 50}\nJob Failed!\nError: {e}\n{'*' * 50}")
            return  f"{'*' * 50}\nJob Failed!\nError: {e}\n{'*' * 50}"


    def get_yang_capabilities(self):
        """
        Get yang capabilities.
        """
        url = f"https://{self.host}:{self.port}/restconf/data/netconf-state/capabilities"
        try: 
            response = requests.get(
                url=url,
                headers=self.headers,
                auth=(self.username, self.password),
                verify=False
            )
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Failed - Status Code: {response.status_code}")
                return f"Failed - Status Code: {response.status_code}"
        except ConnectionError as e:
            print(f"{'*' * 50}\nJob Failed!\nError: {e}\n{'*' * 50}")
            return  f"{'*' * 50}\nJob Failed!\nError: {e}\n{'*' * 50}"
