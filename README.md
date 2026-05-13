
# potyk-mu

> Fav music collection

## Links

- [Github](https://github.com/potykion/potyk-mu-2.git)

## Prod Setup

### First

```shell
ssh-keygen
# example pub
# paste it to https://github.com/settings/keys
cat .ssh/id_ed25519.pub

ssh -l leybovich-nikita 84.201.131.244
# e.g. git@github.com:potykion/wine-wish.git
git clone git@github.com:potykion/potyk-mu-2.git

cd potyk-mu
python3 -m venv ".venv"
source ./.venv/bin/activate
pip install -r requirements.txt
# fill env w FLASK_APP=main & FLASK_SECRET=...
nano .env

sudo cp ./potyk-mu.service /etc/systemd/system/potyk-mu.service
sudo chmod 644 /etc/systemd/system/potyk-mu.service
sudo systemctl enable --now potyk-mu.service

```

### Update

```shell
ssh -l leybovich-nikita 84.201.131.244
cd potyk-mu
git pull
sudo systemctl restart potyk-mu.service
```
