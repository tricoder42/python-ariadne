# coding: utf-8
from __future__ import unicode_literals

import multiprocessing
import socket
import time
from contextlib import closing

from attrdict import AttrDict
from six.moves.urllib.error import URLError, HTTPError
from six.moves.urllib.request import urlopen

from . import Context


class FlaskApp(Context):
    """
    Run Flask App as background process and return server_url of Flask server
    """

    def __init__(self, app, timeout=None):
        self.app = app
        self.port = None
        self.timeout = timeout or 5

        self._process = None

    def __call__(self, context=None):
        if not context:
            context = {}

        self.start()

        context.update({
            'server_url': self.server_url,
        })
        return AttrDict(context)

    def start(self):
        """ Start application in a separate process. """
        self.port = self.get_free_port()

        worker = lambda app, port: app.run(port=port, use_reloader=False)
        self._process = multiprocessing.Process(
            target=worker,
            args=(self.app, self.port)
        )
        self._process.start()

        # Wait for server to start
        for i in range(self.timeout):
            time.sleep(1)
            try:
                urlopen(self.server_url)
            except HTTPError:
                " Server is up, but returns 404 for /"
                break
            except URLError:
                " Server is down, we need to wait."
            else:
                " No error, server is up."
                break

    @property
    def server_url(self):
        """ Returns the complete url based on server options. """
        return 'http://localhost:{0}'.format(self.port or 80)

    def stop(self):
        """ Stop application process. """
        if self._process:
            self._process.terminate()

    def get_free_port(self):
        """ Get free available port for server. """
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.bind(('', 0))
            return s.getsockname()[1]

    def __del__(self):
        """ Stop server process automatically when object is destroyed """
        self.stop()

    def __repr__(self):
        return '<Flask app listening at {0}>'.format(self.server_url)
