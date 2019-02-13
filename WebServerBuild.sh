#
# Ubuntu Web Server Build
# Script can be placed into AWS UserData 
# Loops continuously waiting for firewall to intialise and then loads Apache and PHP
#
#!/bin/bash -ex
until resp=$(curl -s -S -g --max-time 3 --insecure "https://<Firewall IP>/api/?type=op&cmd=<show><chassis-ready></chassis-ready></show>&key=<api key>");do
if [[ $resp == *"[CDATA[yes"* ]] ; then
    break
  fi
  sleep 10s
done  
sudo apt-get update &&
sudo apt-get install -y apache2 php7.0 &&
sudo apt-get install -y libapache2-mod-php7. &&
sudo rm -f /var/www/html/index.html &&
sudo wget -O /var/www/html/index.php https://raw.githubusercontent.com/wwce/Scripts/master/showheaders.php &&
sudo service apache2 restart &&
sudo echo "done"
