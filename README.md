# owl-domoticz
Interface between OWL Intuition-ic and Domoticz

This python scripts listen on UDP 22600 for OWL Intuition IC data push, and send the data to Domoticz using API.

***OWL Intuition portal part :***
On System > Data push
Configure the IP address and port of the host running the script

***Domoticz part :***
1. Create a Dummy Hardware
2. Create a Virtual Sensor of type "Ampere (3 phase)"
3. Write down the index of the Sensor (check Idx column of the Devices panel)
4. Replace idx=19 by idx=your_index_number on the owl.py file

***Script part :***
Replace DOMOTICZ_IP and PORT by your own values

***Using the script :***
- Manually -->
make the script executable & run it : chmod +x owl.py & ./owl.py

- Systemd script -->
Here is a sample systemd script you can use to start the script as a daemon. The owl.py has been moved to /usr/local/bin.
Filename is : /etc/systemd/system/owl-forwarder.service

```
[Unit]
Description=OWL Forwarding to Domoticz
After=syslog.target

[Install]
WantedBy=multi-user.target

[Service]
ExecStart=/usr/local/bin/owl.py
Type=simple
User=domoticz
RemainAfterExit=yes
StandardOutput=syslog
StandardError=syslog
```
