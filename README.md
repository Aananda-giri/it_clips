# Pyclipse
  - Stores text copied to a file
  - application: note while reading text

# usage
`python3 clips.py file_name `

* default file_name : `clip.json`

# Todo:
    - Run at startup
    METHOD 1 :
    append to: /etc/rc.local
    /path/to/my_script.sh &

METHOD2:
sudo nano /etc/systemd/system/pyclipse.service

# /etc/systemd/system/pyclipse.service
[Unit]
Description=Pyclipse Script Service

[Unit]
Description=Pyclipse Script Service

[Service]
ExecStart=/usr/bin/python3 /usr/sbin/pyclipse/clips.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target

* install dependencies
/usr/bin/python3 -m pip install -r /usr/sbin/pyclipse/requirements.txt

* make file executable
chmod +x /usr/sbin/pyclipse/clips.py

* Enable the service: 
sudo systemctl enable pyclipse.service

* start the service
sudo systemctl start pyclipse.service

* check the status of the srevice
sudo systemctl status pyclipse.service



* Service logs
sudo journalctl -u pyclipse.service
    - Metadata: Website_url, title, data_time
    - listen for certain written commands: 
        - switch file
        - switch to keylogger input
        - perform certain actions: personal assistant

