#/bin/bash
export ENV_FILE_LOCATION=./.env.test

# Start mongo db for local development.
docker-compose up -d --build database

# Run Local Tests
pipenv run python -m unittest tests/test_signup.py
pipenv run python -m unittest tests/test_login.py
