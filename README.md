# OpenITD
Idle Telegram Daemon

## Run script

### For each method
1. Copy `proxy.template.py` to `proxy.py` and setup it if need
2. Copy `secret.template.py` to `secret.py` and setup it ([API token and hash](https://core.telegram.org/api/obtaining_api_id))
3. Run `python3 idlegram.py` one time and login

### Method 1. 24/7 run
1. Run `docker image build -t idlegram .`
2. Run `docker container run -d --name idlegram --restart always idlegram`

### Method 2. One-time run
1. Run `pip3 install -r requirements.txt`
2. Run `python3 idlegram.py`

### Dependencies
* Latest version of Telethon: http://telethon.readthedocs.io/en/stable/
