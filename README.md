# HOW TO USE TEMPLATE

- Replace following vars & commands with ur values:
    - `$PROJ` - project name
    - `$HOME` = home dir like `/home/leybovich-nikita`
    - `$PORT` = port where service will run like 5003
    - `ssh -l $USER $IP` - ssh creds like `ssh -l leybovich-nikita 84.201.131.244`
    - `git clone $REPO_URL_SSH` - ssh git repo url `git clone git@github.com:potykion/potyk-stats.git`
- Rename following files & occurrences to ur names:
    - `example.service` - systemctl service
- Create `.env` from `.evn.example` vars
- Create `.venv` & install reqs: `pip install -r requirements-dev.txt`

# $PROJ

> $PROJ_DESC

## Links

- [Github]($REPO_URL)

## Prod Setup

### First

```shell
ssh-keygen
# example pub
# paste it to https://github.com/settings/keys
cat .ssh/id_ed25519.pub

ssh -l $USER $IP
# e.g. git@github.com:potykion/wine-wish.git
git clone $REPO_URL_SSH

cd $PROJ
python3 -m venv ".venv"
source ./.venv/bin/activate
pip install -r requirements.txt
# fill env w FLASK_APP=main & FLASK_SECRET=...
nano .env

sudo cp ./example.service /etc/systemd/system/example.service
sudo chmod 644 /etc/systemd/system/example.service
sudo systemctl enable --now example.service

```

### Update

```shell
ssh -l $USER $IP
cd $PROJ
git pull
sudo systemctl restart example.service
```
