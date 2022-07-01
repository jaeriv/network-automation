from get-device-data import GetDeviceData



if __name__ == "__main__":
    data = GetDeviceData(
        username="", # Username 
        password="", # Password
        host="", # Hostname or IP Address
        port="" # Port
    )
    # data.get_yang_capabilities()
    # data.get_interface_stats()
    # data.get_interface_config()
