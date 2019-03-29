# Cryptocurrency Price Tracker
This site allows users to input their email, checkoff the name of a coin (out of a maximum of 5 coins) and receive an email digest every morning with the prices of the currencies they are watching.

## Setup
- Create a Python virtual environment and run on the terminal:
    ```sh
    pip install -r requirements.txt
    ```

- Edit the `setup.sh` file with the appropriate values

- Apply migrations by running:
    ```sh
    python manage.py migrate
    ```

## Run
- Start the server by running:
    ```sh
    python manage.py runserver 0:8000
    ```

## Cronjob (For periodic updates)
- Open another terminal
- Setup cronjob by running `crontab -e` and inserting this line:
    ```
    * * * * * source <path-to-repo>/setup.sh && python3 <path-to-repo>/manage.py runcrons > ~/cronjob.log
    ```

> Note that `CRONJOB_FREQUENCY` in setup.sh is set in minutes so 120 means the cronjob will run every two hours; 1440 -> every day. Therefore this ENV variable is what you edit to change the frequency of the periodic emails
