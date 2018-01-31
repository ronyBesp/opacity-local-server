# opacity-local-server
Local Django Python Server for Opacity

The Local Server for Opacity is meant to be run with the Opacity iOS app [repo for iOS App](https://github.com/LeronBergelson/Opacity-iOS)
All the information about the Opacity project and its goals, etc.. can also be found on the Opacity iOS App repo.

## Set-Up

To initially set-up the server please follow the following steps:

- `cd into the Opacity-API/opacity folder`
- `python manage.py makemigrations`
- `python manage.py migrate --run-syncdb`
- `python manage.py createsuperuser` -> will allow you to create an admin user

## Setting up Facebook Authentication

By default when users run the local server with the Opacity iOS app [repo for iOS App](https://github.com/LeronBergelson/Opacity-iOS)
they will be able to authenticate via email registration. 

The Opacity server also allows users to use social authentication to login through Facebook.
To set it up when running the serve go to '127.0.0.1:8000/admin' and login with your superuser.
Then go to the 'Social Applications' section and add the Facebook social application.
You will need to provide your Facebook app's keys that can be found in the Facebook App Developer Dashboard.


## Running the Server

To run the local server please cd into the Opacity-API/opacity directory and run the following command

- `python manage.py runserver`

This will run the server at the address `127.0.0.1:8000`

The django admin panel will be accessible at `127.0.0.1:8000/admin` -> this is where you can login with the superuser you created

Now that the server is up and running you can follow the instructions on the Opacity iOS App [GitHub](https://github.com/ronyBesp/opacity-ios-client) page to set-up the app, connect it to the server and run the Opacity project :)


