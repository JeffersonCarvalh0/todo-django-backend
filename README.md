# Todo

A django restful API that performs CRUD operations on Todos with authentication.

# Building
`pipenv` must be installed. Run `pipenv install` from root to install all dependencies.
If you get errors while building psycopg, following [this](https://github.com/psycopg/psycopg2/issues/900#issuecomment-594934895)
might help.

# Running
From the root directory, run `python todo/manage.py runserver` to start the server
at `localhost:8000`. Open it in the browser to see the swagger ui, where the
endpoints can be tested(in order to use the jwt token for authorization, write `Bearer <token> instead of just `<token>` in the authorization pop up)
