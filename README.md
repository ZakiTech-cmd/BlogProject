# BlogProject

## Setup Python Virtual Env with Poetry

1. Ensure you have the Python [Poetry](https://python-poetry.org/docs/#installation) package manager installed on your machine

2. Run `make install` to install python dependencies and setup virtualenv.


## Run Locally

1. Ensure you have PostgreSQL installed, and you have created a database named `blog_project`.
2. Create a '.env' file with environment variables like this:
    ```
    DB_USER=your_local_postgres_user
    DB_PASSWORD=your_local_postgres_password
    ```
3. Go to the `blog_project` dir: `cd blog_project`
4. Run the migrations `poetry run python manage.py migrate`
5. Run the tests `poetry run python manage.py test`
6. Run the server `poetry run python manage.py runserver`

Alternatively, if you don't want to use `poetry run`, you can activate the virtual environment manually with `source .venv/bin/activate`
and run the commands above without `poetry run`.