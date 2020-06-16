# Todo

A django restful API that performs CRUD operations on Todos with authentication.

# Building
## Using `docker-compose`
Simply run `docker-compose up` or `docker-compose up -d` from root and wait until it starts.

## Building it manually
`pipenv` must be installed. Run `pipenv install` from root to install all dependencies.
If you get errors while building psycopg, following [this](https://github.com/psycopg/psycopg2/issues/900#issuecomment-594934895)
might help.

# Running
If you did a manual build, run `pipenv shell` and `python todo/manage.py runserver`
from root to start the server. If you are running it through docker, the server
should already be running. Open `localhost:8000` in the browser to see the
swagger ui, where the endpoints can be tested(in order to use the jwt token
for authorization, write `Bearer <token> instead of just `<token>` in the
authorization pop up)
