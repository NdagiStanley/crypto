sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt
sudo ufw allow 8000
