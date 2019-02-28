Bootstrap a Juiceshop container and Showheaders.php on local Apache to a Ubuntu instance.

Juiceshop will run in a container mapped to / in Apache.
Showheaders will run as /showheaders/index.php


AWS User-data or Azure cloud-init   
#!/bin/bash  
sudo wget -O juicestage.sh https://raw.githubusercontent.com/wwce/Scripts/master/juiceshop/juiceshopstage.sh &&  
sudo chmod 755 juicestage.sh &&  
sudo bash ./juicestage.sh  
