# Device Configurator Framework | Verification | Ben Smogolski

## Verification steps:
1.	From the DEVASC VM console, run: `python3 capstone_main.py`
2.	Select menu option 2
3.	Select menu option 1
4.	Enter username and password

The screenshot below indicates 1) Python code executes without error 2) Current device information was read from the current_device.json file and 3) Successful Netmiko connection to the router, returning interface IP address information.

![verification]("./verification.png") 
