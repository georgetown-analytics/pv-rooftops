# pv-rooftops
Georgetown Data Science PV Rooftops Project

The API is a Django project: https://www.djangoproject.com/

How to run...
1) Naviagte to Django project directory `django_pv` and execute the command `python manage.py runserver`
     -- The DIRS[] settting of the TEMPLATES configuration in `django_pv/settings.py` may have to be changed to read `'DIRS': ['pv/templates'],` 
2) Open web browser and type `http://localhost:8000/pv/?year=#&price=#` replacing #'s with desired variable.
     -- For years <= 2015, pre-extracted, non-predicted values will be used. Everything else is predicted by national isntallation price per watt.
3) Please update requirements.txt as necessary
