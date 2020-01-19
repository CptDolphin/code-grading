# code-grading

### Packages:
* docker@18.03.1-ce
* docker-compose@1.21.1 build 5a3f1a3
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.21.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
* docker-machine@0.14.0 build 89b8332
```
curl -L https://github.com/docker/machine/releases/download/v0.14.0/docker-machine-`uname -s`-`uname -m` >/tmp/docker-machine
chmod +x /tmp/docker-machine
sudo cp /tmp/docker-machine /usr/local/bin/docker-machine
```
* virtualbox
```
sudo apt-get install -y virtualbox
```

### Build image for the dev env, start vm, connect to its docker env, build the image, and start up container
```
docker-machine create default
docker-machine env default
eval $(docker-machine env default)
docker-compose -f docker-compose-dev.yml build
docker-compose -f docker-compose-dev.yml up -d 
```
