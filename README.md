# Device Configurator Framework

### Capstone Proposal | README.md | Ben Smogolski



This project and lab will challenge students to implement a menu-driven network device management application. The lab uses Python, RESTCONF, and Netmiko libraries to interact with network devices through the command line interface. Emphasis is placed on logical menu structure, flexible design, and modularity. The objective of the lab is to establish a solid framework for a comprehensive network automation application. The concept of extendable menus and submenus will be explored. Students will call functions from secondary Python scripts through import statements. Device inventories and details are stored as text files but are retrieved dynamically. The finished lab will implement basic Cisco IOS functions (no advanced networking knowledge is required). Upon completing the lab, students will be able to add functions and menu options without needing to re-write existing code. Ideas for improved modularity will be explored as well.



#### Project Structure:



The expected Python file structure is as follows...



/capstone-project
	capstone\_main.py
	capstone\_dev\_mgt.py
	capstone\_inv\_mgt.py
	get\_current\_device.py
	current\_device.json
	device\_list.json
	/cisco\_cmd
		show\_ip\_int\_br.py
		show\_ver\_uptime.py
		(...other Cisco IOS scripts)



#### Design Rationale:



Only one Python script is called by the user (capstone\_main.py). This is the main menu which presents the user with two programming modes: Device Management and Inventory Management. Device Management is responsible for interacting with a singular device. Inventory Management is responsible for maintaining device lists which may be supplied to Device Management functions. Only select modules and functions will be implemented in this lab. The primary goal is to build a small but functional system that can be expanded and changed as needed. With some effort, the application may be suitable for use in a production environment.



#### Learning Objectives:



(80%) Students will build a working Python application and gain knowledge of interactive menu commands under the guise of network device administration. A dynamic, user-driven menu system with functional commands will be implemented using Linux, Python, Netmiko, RESTCONF, and Cisco CLI (CSR1000v). Students will gain experience with reusable code rather than bulky, monolithic scripts. Improved error handling and fault isolation are demonstrated through the modular project structure. The lab also demonstrates basic differences between Netmiko/SSH and RESTCONF methods. Device security is upheld using getpass() instead of text files. Devices are referenced and administered via IP addresses specified in the current\_device.json dictionary file.



(20%) Students will conceptually explore options for improving functionality and modularity given the completed framework.



#### Prerequisites:



##### Python 3 environment with text editor...



&#x09;python –version

#### 

##### Netmiko and Requests libraries...



&#x09;pip install netmiko
	pip install requests

#### 

##### Cisco CSR 1000v router with the following commands...



&#x09;enable
	config terminal
	ip http secure-server
	remote-management
	restful-api

