from werkzeug.exceptions import NotFound
from threading import Lock


class CompositeApplication(object):

    def __init__(self, root_application, configuration):

        assert root_application is not None, 'A root application is required for CompositeApplication.'
        self.domain = configuration.DOMAIN
        self.configuration = configuration
        self.lock = Lock()
        self.instances = {}

        self.register_application('', root_application)

    def get_application(self, host):

        host = host.split(':')[0]
        assert host.endswith(self.domain), \
            'Configuration error, please ensure domain/host matches. Current domain is: %s' % self.domain
        subdomain = host[:-len(self.domain)].rstrip('.')

        with self.lock:
            application = self.instances.get(subdomain)
            if application is None:
                return NotFound()
            return application

    def register_application(self, subdomain, application):
        application.config.from_object(self.configuration)
        with self.lock:
            self.instances[subdomain] = application

    def __call__(self, environ, start_response):
        app = self.get_application(environ['HTTP_HOST'])
        return app(environ, start_response)