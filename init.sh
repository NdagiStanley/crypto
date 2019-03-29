#!bin/bash

# Install pip
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip

# Create python virtual environment
pip3 install virtualenv
virtualenv ENV
source ENV/bin/activate

# Clone repo
git clone https://github.com/NdagiStanley/crypto
cd crypto

# Install python requirements
pip3 install -r requirements.txt

# Allow incoming tcp packets on port 8000
sudo ufw allow 8000

# Edit setup.sh and set environment variables
source setup.sh

# Apply migrations
python manage.py migrate

# Setup cronjob by running `crontab -e` and inserting this line:
# Refer https://crontab.guru/#*_*_*_*_*
# Note `CRONJOB_FREQUENCY` in setup.sh is set in minutes so 120 means the cronjob will run every two hours; 1440 -> every day
* * * * * source ~/crypto/setup.sh && python3 ~/crypto/manage.py runcrons > ~/cronjob.log

# Run server
sh run.sh
