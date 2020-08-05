#/bin/bash
export ENV_FILE_LOCATION=./.env

# Start mongo db for local development.
docker-compose up -d --build database

# Start the app for local development.
# You can run the app with docker-compose also
# but its fater to develop running it with local pipenv.
pipenv run python run.py
