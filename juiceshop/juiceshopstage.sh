#!/bin/bash

# Add docker key and repository
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D &&
sudo echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list &&


# Install apache and docker
sudo apt-get update -q &&
sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -q -y -u  -o Dpkg::Options::="--force-confdef" --allow-downgrades --allow-remove-essential --allow-change-held-packages --allow-change-held-pack$
sudo apt-get install -qy apache2 docker-engine php7.0 libapache2-mod-php7.2 &&

# Put the relevant files in place
sudo wget -O /etc/apache2/sites-available/000-default.conf https://raw.githubusercontent.com/wwce/Scripts/master/juiceshop/juiceshopdefaultsite.conf &&
# sudo cp /tmp/juice-shop/default.conf /etc/apache2/sites-available/000-default.conf
sudo mkdir /var/www/html/showheaders/ &&
sudo wget -O /var/www/html/showheaders/index.php https://raw.githubusercontent.com/wwce/Scripts/master/showheaders.php  &&

# Download and start docker image with Juice Shop
sudo docker run --restart=always -d -p 3000:3000 --name juice-shop bkimminich/juice-shop &&

# Enable proxy modules in apache and restart
sudo a2enmod proxy_http &&
sudo systemctl restart apache2.service &&

# Run shake.js/logger
sudo docker run --restart=always -d -p 8080:80 --name shake-logger -e TARGET_SOCKET=192.168.33.10:8080 wurstbrot/shake-logger
