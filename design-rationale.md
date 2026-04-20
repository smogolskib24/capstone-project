# Device Configurator Framework
## Capstone Design Rationale v1.0

### Overview

The assignment is to “...design, implement, and document a complete instructional automation lab suitable for undergraduate networking students.” (Pickard, 2026). The context for this assignment is derived from the Cisco Networking Academy DevNet Associate course; students will “...sharpen [their] development skills…”, and “...gain a comprehensive understanding of infrastructure automation…” (Cisco Netacad, DevNet, n.d.). These two sources, together with the author’s own experiences, motivators, and presuppositions form the basis of the Device Configurator Framework Lab (the “Project”). Importantly, the application has the potential to query and configure network devices in various ways, but these hypothetical functions are not the focus of the lab. Rather, the lab provides the framework while students get an opportunity to recommend future improvements.

### Student Experience and Learning Outcomes

The overarching vision for this lab is to provide the student with a sense of accomplishment. Students are able to build something from scratch and then use it. Moreso, the Project provides a tactile experience as keyboard inputs result in visual feedback from the device and/or application. The Project’s menu system provides students with a sense of choice and freedom; while building the application, options are enumerated but there is no formal “lock in”. The application can be fully customized to suit anyone’s job assignments or curiosity. Within approximately 75 minutes, students are not just working with Cisco APIs, they are experiencing a “lite” version of the entire software development process. 

Upon completing the lab, students will have been exposed to a number of interconnected concepts and components: Python, Netmiko, SSH, JSON, and the Cisco CLI. The overall learning outcome is for students to gain experience executing basic Cisco CLI commands remotely. This sets the stage for future automation tasks and APIs, where the administrator does not directly “touch” the device. 

Approximately 20% of this lab is set aside for the conceptual improvements of the framework. This is important because most software development projects are never truly completed.

### Python Language with Netmiko and Requests Libraries

The Project uses the Python scripting language exclusively, as Python is touted as one of the most popular programming languages in the world (Cisco NetAcad, Python, n.d.). Cisco further claims that Python is “Easy to learn… teach… use… understand… and obtain” (Cisco NetAcad, Python, n.d.). Further, Netmiko is used due to its simplicity and widespread industry acceptance. After importing ConnectHandler from Netmiko, we require just four lines of functional code:

```
with ConnectHandler(**var_router) as conn:
net_connect = ConnectHandler(**var_router)
output = conn.send_command('show ip interface brief')
net_connect.disconnect()
```

(Additional code is used to print and format the output).

### The Use of JSON

This lab uses the JSON format to store device information within a text file. Python dictionaries and JSON have a symbiotic relationship because they are visually interchangeable. We use json.load() to read the device information from the text file and assign it as current_device. We then print the device IP address by accessing elements of the dictionary (`var_router[“host”]`).

### Project Structure

The file structure of the Project coincides with the modular, menu-driven application design. Each menu sub-function is imported from a separate file, as noted at the top of each script (e.g. from get_current_device import get_current_device). We chose to selectively import functions using the from keyword; this was a random design choice and not a requirement. Alternatively, students can import entire modules and call functions by prefixing them with the module name (get_current_device.get_current_device()).

### Scope and Time Commitment

Initially, the lab appears to be a lengthy endeavour and may be intimidating once students learn that multiple files and functions will be created. There are two mitigating factors: 1) limited number of lines per file, and 2) advocating a copy and paste approach. Additionally, two of the functions/files can be skipped for time (show_ver_uptime.py and interfaces_rest.py). This lab demonstrates that functions are commodities; they can be added and removed as the situation demands. The important lesson is about incorporating them into a larger design.

### Menu System

The lab’s primary feature is its text-based menu system. This is a departure from a simple “one shot” Python script. Menus give the operator a sense of direction and control. As presented, the menu is hierarchical, starting with the Main Menu which presents two modules. The first module is Inventory Management; functions that manage a device inventory or fleet. The second module is Device Management which is the primary focus of the lab. Device Management contains the subsequent Cisco commands that students will implement. Importantly, the menu options are numbered which gives the impression of expandability. For a fully developed application, students would likely implement double digit integers (e.g. 05, 06, 13) to maintain a visually consistent experience. 

Further, the menu system allows students to 1) go back to the previous menu and/or 2) quit the application. This provides a persistent experience without the feeling of being trapped:

```
print("*** MAIN MENU ***" + "\n" "________" + "\n")
print("1. Inventory Management" + "\n" + "2. Device

Management" + "\n" + "9. Quit" + "\n" + "________\n")

#########

print("*** DEVICE MANAGEMENT MODE ***" + "\n" "________" +
"\n")

print("1. show ip int br" + "\n" + "2. show ver uptime" +
"\n" + "3. interfaces-state (REST)" + "\n" + "9. Return to Main" + "\n" + "________\n")
```
### Safety and Error Handling

As presented, the Configurator Framework is unquestionably safe to run because it does not include configuration commands, nor does it possess the innate ability to modify device configurations. The three Cisco functions presented in the lab are read-only and do not require a persistent connection. However, there are two possible ways for the application to become “unsafe”:

The student adds their own read-write commands/modules to the application,
The script becomes a “runaway” process, creating a denial of service scenario for the router.

Device credentials are protected by utilizing interactive logins rather than hard-coded credentials. Students must type in usernames and passwords for each connection to the router. The getpass() module is used to conceal the typed password.

Basic error handling comes in the form of try: and except: blocks within the code. Although error handling is not a focus of this lab, the modular nature of the project lends itself well to error containment methods. For example, errors can be reported based on the location of the function rather than the location of the initially called script.

### Improvements & Reflections

Four questions are asked at the end of the lab to reinforce learning. The first three questions are open ended to inspire creativity rather than objectivity. The last question ensures that students understand the modular design. We intentionally try to avoid technical questions regarding Python, Netmiko, REST, or Cisco IOS. 

### Limitations

The Project is intentionally limited in terms of its ability to modify device configurations. Creating complex and potentially unsafe Cisco commands within the context of this lab would be distracting and time consuming. Moreso, the Project is not intended to be a Python programming lesson. There are likely multiple ways to improve upon the code. Stacking/chaining modules and functions creates obscurity and risks which are not disclosed in this Project. DevOps validation methods are not part of this lab.

A fully developed Device Configurator application should have an application user login and corresponding credential database which is not included in this lab. At the time of writing, the code is not commented; this document and other supporting materials take the place of in-code commentary. Students are encouraged to comment on their code, especially in production scenarios.

This lab does not include any information or references to NETCONF, a popular automation/management protocol. Finally, this lab does not use Ansible, Puppet, Chef, Terraform, or any 3rd party automation platforms.

### Conclusion

The Device Configurator Framework lab takes a “macro” approach to network automation by wrapping functions into a flexible menu structure. Students will hopefully learn that simple Python scripts can be transformed into a tactile experience. 

### References:

Pickard, J. (2026). ICTN 6875 Capstone Project Instructions. East Carolina University.

DevNet Associate. (n.d.). Cisco Netacad.
https://www.netacad.com/courses/devnet-associate?courseLang=en-US

Python Essentials 1. (n.d.). Cisco Netacad.
https://www.netacad.com/courses/python-essentials-1


