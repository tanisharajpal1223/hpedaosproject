# hpedaosproject
Distributed Asynchronous Object Storage [DAOS]
Introduction

What is DAOS?
DAOS is an open-source, high-performance object storage system designed to leverage Intel® Xeon® processors, Intel® Optane™ Persistent Memory, and NVMe SSDs. This tool sets up DAOS in a VM environment using tmpfs to emulate storage.

🔧 Features
Automates DAOS server and agent startup

Performs storage formatting using tmpfs

Queries DAOS system and storage status

Creates and manages storage pools

Written in Python for extensibility and easy scripting

🖥️ Requirements
CentOS 7.9 or compatible Linux VM

Python 3.6+

DAOS 2.0 installed (daos-server, daos-agent, dmg)

sudo privileges on the VM

📁 File Structure
bash
Copy
Edit
.
├── daos_interaction.py     # Python script to control and query DAOS
├── README.md               # This documentation file
└── (DAOS config files)
🚀 How to Run
Install DAOS following the DAOS Quickstart Guide.

Ensure all DAOS services are configured correctly:

/etc/daos/daos_server.yml

/etc/daos/daos_control.yml

/etc/daos/daos_agent.yml

Mount tmpfs as SCM:

bash
Copy
Edit
sudo mkdir /mnt/daos0
sudo mount -t tmpfs -o size=64G tmpfs /mnt/daos0
Run the Python script:

bash
Copy
Edit
python3 daos_interaction.py
📋 What It Does
Step	Description
Start Server	Launches the DAOS server systemd service
Start Agent	Launches the DAOS agent
Format Storage	Formats tmpfs-based SCM using dmg
Query System	Verifies DAOS system membership and health
Query Storage	Displays usage statistics
Create Pool	Creates a new 1GB storage pool named test_pool

🛠️ Example Output
bash
Copy
Edit
[+] Starting DAOS server...
[+] Starting DAOS agent...
[+] Formatting DAOS storage...
Format Summary:
  Hosts                 SCM Devices NVMe Devices
  -----                 ----------- ------------
  localhost.localdomain 1           0
[+] Querying DAOS system state...
[+] Creating DAOS pool 'test_pool' of size 1G...
📚 Resources
DAOS Documentation
