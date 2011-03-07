# -*- coding: utf-8 -*-
"""WSGI app setup."""
import os
import sys

if 'lib' not in sys.path:
    # Add lib as primary libraries directory, with fallback to lib/dist
    # and optionally to lib/dist.zip, loaded using zipimport.
    sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']

from tipfy import Tipfy
from config import config
from urls import get_rules


def enable_appstats(app):
    """Enables appstats middleware."""
    from google.appengine.ext.appstats.recording import \
        appstats_wsgi_middleware
    app.wsgi_app = appstats_wsgi_middleware(app.wsgi_app)


def enable_jinja2_debugging():
    """Enables blacklisted modules that help Jinja2 debugging."""
    if not debug:
        return

    # Enables better debugging info for errors in Jinja2 templates.
    from google.appengine.tools.dev_appserver import HardenedModulesHook
    HardenedModulesHook._WHITE_LIST_C_MODULES += ['_ctypes', 'gestalt']


debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
sys_config = config.get('momentum.fatcatmap')

app = Tipfy(rules=get_rules(), config=config, debug=debug)

if sys_config.get('enable_hooks', False) == True:
	if debug:
		enable_jinja2_debugging()
	if sys_config['enable_hooks'].get('appstats', False) == True:
		enable_appstats(app)

def main():
    # Run the app.
    app.run()


if __name__ == '__main__':
    main()
