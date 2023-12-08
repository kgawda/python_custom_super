# Deployment

Przygotowanie:
```bash
scp -r web_app admin@_______:
ssh admin@_____ sudo apt install -y python3.11-venv
ssh admin@_____ python -m venv deploy_venv
ssh admin@_______ deploy_venv/bin/pip install -r web_app/requirements.txt
```

Bardzo uproszczone odpalenie
```bash
ssh admin@____ deploy_venv/bin/python web_app/main.py
# strona internetowa poinna się pojawić na adresie http://____:5000
ssh admin@_____ killall deploy_venv/bin/python
```

Odpalenie przez systemd:
```bash
scp -r web_app admin@_______:
ssh admin@_____ sudo cp web_app/webapp.service /etc/systemd/system/
ssh admin@_____ sudo systemctl start webapp
# strona internetowa poinna się pojawić na adresie http://____:5000
ssh admin@_____ sudo systemctl status webapp
```
