from importlib import import_module

from flask import Flask

from foursquare_sample import settings
from foursquare_sample.settings import VIEWS
from foursquare_sample_util.constants import Settings


def create_app(config):
    app = Flask(__name__)

    if config is not None:
        configuration = getattr(settings, config + Settings.CONFIG_SUFFIX)
        app.config.from_object(configuration)

    return app


def __register_blueprints(app):
    views = [import_module('%s.%s' % (module_name, Settings.VIEWS)) for module_name in VIEWS]
    for view in views:
        app.register_blueprint(view.blueprint)
