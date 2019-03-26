sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt
python manage.py collectstatic
sudo ufw allow 8000


export SECRET_KEY=""
export API_KEY_COINMARKET=""
export EMAIL_HOST_USER=""
export EMAIL_HOST_PASSWORD=""

0 6 * * * * python3 ~/crypto/manage.py runcrons > ~/cronjob.log
