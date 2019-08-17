# Unicornis Challenge - Meeting Scheduler

As a part of a job application process, i am tasked to make a meeting scheduler utilizing the Django and Bootstrap technologies.
The goal of development is to be able to have a model-layer able to:
* **Handle** users
* **Create** meetings
* **Create** matters/issues & **log** decisions
* **Link & serve** documentation to matters/issues
* **Invite** users to meetings via email & **Log** invitation responses, attendance

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project relies on having Python 3.7.0. from [downloads](https://www.python.org/downloads/) and [pipenv](https://pipenv.readthedocs.io/en/latest/install/) to help you manage dependencies and virtual environments.

### Installing

When you have cloned and entered the repository, run:

```bash
$ pipenv install
```
to install dependencies.

## Deployment

To deploy the system locally you must first:

* run the virtualenvironment:

```bash
$ pipenv shell

```

then navigate to:

```bash
$ cd src
```

and run the Django server:

```bash
$ python manage.py runserver [port(default=8000)]
```

you can then find the server running in your browser at given port

## Built With

* [Django2.2](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/) - The frontend magic shop

## Some things bout style

In this project i am aiming to develop a service that is as modular as possible. This hopefully results in Django-classes being as small as i can make them, so that i might be able to reuse them at a later point in time. If a Django class has more than 3 models, they should be saved as individual Python files and made known to app/models/`__init__.py`

## Project Structure

Every Django app must function independently.
Every Django app should have this structure:

```bash
your_app/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations
        │   └── __init__.py
        ├── models
        │   ├── __init__.py
        │   ├── model1.py
        │   └── ...
        ├── templates
        │   ├── model1/
        │   │         ├──somename.html #be practical
        │   │         └──othername.html #and so on
        │   └── base.html
        ├── tests.py
        └── views.py
```

If one needs to use something to make the apps work together, then put this in
the /src/core app.


### meeting_scheduler
The main Django app containing only code relevant to running the django service, URLconf and deciding Django behavior relevant to the project.

###website_wrapper
Is the wrapper of the web-app, makes everything pretty.

### users
A custom user class utilizing a custom user model built on top of [django.contrib.auth.models](https://docs.djangoproject.com/en/2.2/ref/contrib/auth/#user-model)'s AbstractUser class, as requested by the [documentation](https://docs.djangoproject.com/en/2.2/ref/contrib/auth/#user-model) when crating custom users in a new project. This class also handles authorization and creation of users  

####Models:

####Views:

### custom_groups
TBA




###Templates:
* login.html
* signup.html

As of now this class is identical to the usual


## Contributing

Feel free to make a pull request, if i find it great i will include it and your authorship.

## Authors

* **Tor-Aksel Solberg** - *Initial work* - [PurpleBooth](https://github.com/torakses)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thank you to Unicornis who challenged me to discover web-development
