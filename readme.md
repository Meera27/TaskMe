manage.py is a command-line utility used to run the server, migrations, and admin tasks.

A Django project can have multiple apps. Apps make the code modular and reusable.

Each model = one DB table
Fields = columns

Django models are Python classes that map directly to database tables using the ORM.

MIGRATIONS (DB CREATION)

## python manage.py makemigrations
### python manage.py migrate


Migrations track model changes and apply them safely to the database.

Django Admin provides a built-in UI to manage application data without writing custom code.

## python manage.py createsuperuser

# Task.objects.all(): 
Fetches all records from the database table associated with the Task model.

# .values(): 
Transforms the result from a QuerySet of model instances into a QuerySet of dictionaries, where keys are column names and values are the data. 

# Returns: <QuerySet [{'id': 1, 'title': 'Task 1', ...}, {'id': 2, 'title': 'Task 2', ...}]>
tasks = Task.objects.all().values()

Django follows MVT architecture where URLs route requests to views, views interact with models, and responses are returned to the client.