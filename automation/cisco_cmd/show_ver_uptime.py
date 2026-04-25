from netmiko import ConnectHandler
from get_current_device import get_current_device
import getpass

var_router = get_current_device()

def show_ver_uptime():

   while True:
       
    try:
            usernm = input("Username: ")
            passwd = getpass.getpass("Password: ")
            var_router["password"] = passwd
            var_router["username"] = usernm

            with ConnectHandler(**var_router) as conn:

                print("Connecting to: " + var_router["host"])
            
                net_connect = ConnectHandler(**var_router)
                output = conn.send_command('show ver | inc uptime')
                print(output[:500] + "\n")
                net_connect.disconnect()
                break
        
    except:
            print("Unexpected Error in: show_ver_uptime")
            break