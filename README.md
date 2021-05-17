# MathStudyingPlatform-test

For running on your own device follow the next steps:
1. Make sure that you have python3.8 on your local machine
2. Clone this repository
3. Go in project directory
4. Setup environment `python3.8 -m venv venv`
5. Use environment `source venv/bin/activate`
6. Install requirements `pip install -r requirements.txt`
7. Run PostgreSQL server in the background `docker-compose up --detach`
8. Run migration files `make migrate`
9. Run application `make run`
