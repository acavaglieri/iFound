# run with docker compose

## Install Docker

https://docs.docker.com/compose/install/linux/#install-using-the-repository

Then:

```
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo systemctl start docker
sudo systemctl status docker
```

## Start

```
./run.sh restart
```