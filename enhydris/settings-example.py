# Django settings for enhydris project.
# coding=UTF-8
from django.utils.translation import ugettext_lazy as _
import os.path

ENHYDRIS_PROGRAM_DIR = os.path.dirname(__file__)

# Leave following three lines as they are, to import several Django settings.
execfile(os.path.join(ENHYDRIS_PROGRAM_DIR, 'settings-base.py'))

DEBUG = True
TEMPLATE_DEBUG = False
STATIC_SERVE = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES =  {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'enhydris_test',
        'USER': 'enhydris',
        'PASSWORD': 'changeme',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

TIME_ZONE = 'Europe/Athens'

SITE_ID = 1
SITE_URL = "hydroscope.gr"

MEDIA_ROOT = 'site_media/'
MEDIA_URL = '/site_media/'
STATIC_ROOT = 'static/'
STATIC_URL = '/enhydris-static/'

GRAPPELLI_ADMIN_TITLE = 'Enhydris Administration'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'yy)g)w2jqkpyv9$w39i9$7(6wb+$h(_+x3gj#=@fzs2tmuj$#='

# GentityFile upload directory (must be relative path and it'll be created
# under site_media dir)
GENTITYFILE_DIR = 'gentityfile'

#Uncoment to hide open layers map
#USE_OPEN_LAYERS = False
#Uncoment to alter the default value of min viewport
#MIN_VIEWPORT_IN_DEGS = 0.04
#Map default area (minlong, minlat, maxlong, maxlat)
MAP_DEFAULT_VIEWPORT = (19.3, 34.75, 29.65, 41.8)

# Options for django-registration
ACCOUNT_ACTIVATION_DAYS=7
EMAIL_USE_TLS = True
EMAIL_PORT=587
EMAIL_HOST='smtp.my.domain'
DEFAULT_FROM_EMAIL = 'user@host.domain'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST_USER='automaticsender@my.domain'
EMAIL_HOST_PASSWORD='mypassword'

#Set login redirection as apropriate in the cases
#of site installed on a subdirectory
#for http://my.site/my_dir/ set it to /my_dir/
#LOGIN_REDIRECT_URL='/my_dir/'
#If you uncomment the above line, please uncomment
#the line bellow as well to update LOGIN_URL correctly
#LOGIN_URL=LOGIN_REDIRECT_URL+'accounts/login'

#Change SESSION_COOKIE_NAME if more than one django
#sites on a single domain, or other sites with
# sessionid is already set (defaul: sessionid)
#SESSION_COOKIE_NAME='sessionid'

#Set custom cookies expiration (default is 2 weeks
#that is 1209600 seconds).
#SESSION_COOKIE_AGE=2419200

# Options for political divisions
FILTER_DEFAULT_COUNTRY= 'GREECE'
FILTER_POLITICAL_SUBDIVISION1_NAME= _('District')
FILTER_POLITICAL_SUBDIVISION2_NAME= _('Prefecture')

USERS_CAN_ADD_CONTENT=False
SITE_CONTENT_IS_FREE=False
TSDATA_AVAILABLE_FOR_ANONYMOUS_USERS=False
STORE_TSDATA_LOCALLY=True

#REMOTE_INSTANCE_CREDENTIALS = {'kyy.hydroscope.gr': ('myusername', 'mypassword')}

#Display copyright information on web pages (station detail and time
#series detail)
DISPLAY_COPYRIGHT_INFO=False

#This is a way to filter all station data site_wide with some
#criteria.
#SITE_STATION_FILTER = {'owner__id__exact': '9',}