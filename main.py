import sys
sys.path.insert(0, "lib")

from middleware import CompositeApplication
from blog import views
from aedigital import aedigital
from configuration import AppConfig


application = CompositeApplication(aedigital.application, AppConfig)
application.register_application(AppConfig.BLOG_SUBDOMAIN, views.application)