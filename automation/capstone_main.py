from capstone_inv_mgt import inv_main
from capstone_dev_mgt import dev_main

def main():
    while True:

        try:

            print("*** MAIN MENU ***" + "\n" "________" + "\n")

            print("1. Inventory Management" + "\n" + "2. Device Management" + "\n" + "9. Quit" + "\n" + "________\n")
            
            user_input = input("Selection: ")
            user_input = int(user_input)
                            
            if user_input == 1:
               inv_main()
            elif user_input == 2:
               dev_main()
            elif user_input == 9:
                print("Goodbye.")
                break
            else:
                print("Invalid number. Try again.")

        except:
            print("Error: Invalid Entry.")

if __name__ == "__main__":
    main()