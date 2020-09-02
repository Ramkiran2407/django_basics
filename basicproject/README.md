## Deployement in Python Anywhere


### THROUGH GIT REPOSITORY


1. Open Bash Console in python anywhere

2. Clone the git code from git hub through SSH / HTTP link

3. Create Virtual Environment.

 Command : mkvirtualenv --python=/usr/bin/python3.6(any python version) <any virtual env name>
 
4. if you have requirments.txt file install all packages.

command: pip install -r requirments.txt

To generate requirments.txt file command "pip freeze > requirments.txt"

5. Go to Web in python anywhere webpage.

6. Set your Environment path by entering <virtualenv name>. 

7. Configure WSGI FILE 


#wsgi.py file

<!-- # import os
# import sys

# path = "/home/VRamaKiran/django_basics/basicproject" (Path where you clone your application)
# if path not in sys.path:
#     sys.path.insert(0, path)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'basicproject.settings' (<projectname>.settings)
# from django.core.wsgi import get_wsgi_application
# from django.contrib.staticfiles.handlers import StaticFilesHandler
# application = StaticFilesHandler(get_wsgi_application()) -->


ONCE we done with everything make change in project/settings.py file (ALLOWED_HOST=['*' or respective hostname in string])

----- DONE WITH YOUR APPLICATION ----

if you wanna add template and static pages clone those


commands: 
python manage.py collectstatic

And add those changes in WEB(python anywhere).


 
 
For Images or Static \ Media folder need to add few lines in settings.py file

<!-- MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') -->


In urls.py file


<!-- from django.conf.urls.static import static -->


<!-- +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) -->
