# -*- coding: utf-8 -*-
from robot.api import logger

import os
import signal
import subprocess

__version__ = '1.0'
ROBOT_LIBRARY_DOC_FORMAT = 'reST'


class WebpackLibrary:
    """WebpackLibrary is a library to start and stop Webpack Dev Server.
    """

    webpack_pid = None

    # TEST CASE => New instance is created for every test case.
    # TEST SUITE => New instance is created for every test suite.
    # GLOBAL => Only one instance is created during the whole test execution.
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, host="0.0.0.0", port=8000, path='.', content_base='dist', debug=False):
        """WebpackLibrary can be imported with optional arguments.

        `host` is the hostname webpack dev server will bind to. Default value
        is '127.0.0.1'.

        `port` is the port webpack dev server will listen. Default value is
        8000.

        Examples:
        | Library | Selenium2Library | timeout=15        | implicit_wait=0.5  | # Sets default timeout to 15 seconds and the default implicit_wait to 0.5 seconds. |  # noqa
        | Library | WebpackLibrary   | 127.0.0.1         | 55001              | path=mysite/mysite | manage=mysite/manage.py | settings=mysite.settings | db=mysite/db.sqlite3 | # Sets default hostname to 127.0.0.1 and the default port to 55001.                |  # noqa
        """
        self.host = host
        self.port = port
        self.path = os.path.realpath(path)
        self.content_base = 'dist'
        if debug.lower() == 'true':
            self.debug = True
        else:
            self.debug = False

    def start_webpack(self):
        """Start Webpack Dev Server."""
        logger.console("-" * 78)
        args = [
            'webpack-dev-server',
            '--inline',
            '--bail',
            '--port={}'.format(self.port),
            '--content-base=%s' % self.content_base,
        ]
        self.webpack_process = subprocess.Popen(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            cwd=self.path,
        )
        self.webpack_pid = self.webpack_process.pid
        with self.webpack_process.stdout:
            for line in iter(self.webpack_process.stdout.readline, b''):
                if self.debug:
                    logger.console(line)
                    print line
                if 'bundle is now VALID' in line:
                    logger.console(
                        "Webpack Dev Server ready (PID: %s)" % self.webpack_pid,
                    )
                    logger.console("-" * 78)
                    break

    def stop_webpack(self):
        """Stop Webpack Dev server."""
        os.kill(self.webpack_pid, signal.SIGKILL)
        logger.console(
            "Webpack Dev Server stopped (PID: %s)" % self.webpack_pid,
        )
        logger.console("-" * 78)
