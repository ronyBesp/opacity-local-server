# opacity-local-server
Local Django Python Server for Opacity

## Set-Up

To initially set-up the server please follow the following steps:

- `cd into the Opacity-API/opacity folder`
- `python manage.py makemigrations`
- `python manage.py migrate --run-syncdb`
- `python manage.py createsuperuser` -> will allow you to create an admin user


## Running the Server

To run the local server please cd into the Opacity-API/opacity directory and run the following command

- `python manage.py runserver`

This will run the server at the address `127.0.0.1:8000`

The django admin panel will be accessible at `127.0.0.1:8000/admin` -> this is where you can login with the superuser you created

Now that the server is up and running you can follow the instructions on the Opacity iOS App [GitHub](https://github.com/ronyBesp/opacity-ios-client) page to set-up the app, connect it to the server and run the Opacity project :)


