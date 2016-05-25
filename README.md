# django-social-auth
An example of Django social authentication

## Overview
These code snippets have been taken from a larger SaaS Django project launching in the summer of 2016.  Users can either be invited to join an existing company's account on the platform or they could be an entirely new user/company.

To add a new employee to an existing company on the system an adminstrator simply adds an employee on their website and sends them an invite to join the service.  When the employee logs in using their Google, Facebook or Twitter account the system will recognise them by their email address and associate them with the existing company.  In the background the django-social-auth module handles the authentication with the third party and creates a Django user record.  pipeline.py then associates the Employee record with the Django User record.

In the case of new users which haven't previously received an invite pipeline.py will redirect the user to a company registration page allowing the user to enter their company details and start using the service.

## Getting started
To get up and running with django social authentication:

* ```pip install django-social-auth```
* Sign up for a Google API key (or Twitter, Facebook etc.)
* Merge the changes contained in settings.py, models.py and urls.py into your own project
* Add the API keys into settings.py
* Add views.py, pipeline.py and register.html to your project
* Change myapp to your application name where appropriate
* Change the Company and Employee names if necessary

 