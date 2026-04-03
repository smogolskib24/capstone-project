from get_current_device import get_current_device
from cisco_cmd.show_ip_int_br import show_ip_int_br
from cisco_cmd.show_ver_uptime import show_ver_uptime
from cisco_cmd.interfaces_rest import interfaces_rest

def dev_main():
    
    while True:

        try:

            print("*** DEVICE MANAGEMENT MODE ***" + "\n" "________" + "\n")

            var_router = get_current_device()

            print("Current Device: "+ var_router["host"])
                                                              
            print("1. show ip int br" + "\n" + "2. show ver uptime" + "\n" + "3. interfaces-state (REST)" + "\n" + "9. Return to Main" + "\n" + "________\n")
            
            user_input = input("Selection: ")
            user_input = int(user_input)

            if user_input == 1:
               show_ip_int_br()
            elif user_input == 2:
               show_ver_uptime()
            elif user_input == 3:
               interfaces_rest()
            elif user_input == 9:
                print("Going back to Main.")
                break
            else:
                print("Invalid entry! Try again.")
            
        except:
            print("Unexpected error in: dev_main")
            break
