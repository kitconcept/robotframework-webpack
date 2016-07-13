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
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        """WebpackLibrary can be imported with optional arguments.
        """
        pass

    def start_webpack(self, host="0.0.0.0", port=8000, path='.', content_base='dist', config=False, debug=False):
        """Start Webpack Dev Server."""
        self.host = host
        self.port = port
        self.path = os.path.realpath(path)
        self.content_base = os.path.realpath(content_base)
        self.config = config
        if debug.lower() == 'true':
            self.debug = True
        else:
            self.debug = False
        logger.console("-" * 78)
        args = [
            'webpack-dev-server',
            '--inline',
            '--bail',
            '--port={}'.format(self.port),
            '--content-base=%s' % self.content_base,
        ]
        if self.config:
            full_path = '{}/{}'.format(self.path, self.config)
            if not os.path.isfile(self.config):
                logger.console(
                    'ERROR: Could not find Webpack configuration {}'.format(
                        full_path
                    )
                )
                return
            args.append('--config')
            logger.console(full_path)
            args.append(full_path)

        try:
            self.webpack_process = subprocess.Popen(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=1,
                cwd=self.path,
            )
        except OSError as e:
            logger.console('ERROR: Fail to call webpack {}'.format(e))
        self.webpack_pid = self.webpack_process.pid

        stdout = []
        with self.webpack_process.stdout:
            for line in iter(self.webpack_process.stdout.readline, b''):
                if self.debug:
                    logger.console(line)
                    stdout.append(line)
                if 'bundle is now VALID' in line:
                    logger.console(
                        "Webpack Dev Server ready (PID: %s)" % self.webpack_pid,
                    )
                    logger.console("-" * 78)
                    break
        if stdout:
            return

        logger.console('ERROR: Webpack could not be started')
        with self.webpack_process.stderr:
            for line in iter(self.webpack_process.stderr.readline, b''):
                logger.console(line)

    def stop_webpack(self):
        """Stop Webpack Dev server."""
        os.kill(self.webpack_pid, signal.SIGKILL)
        logger.console(
            "Webpack Dev Server stopped (PID: %s)" % self.webpack_pid,
        )
        logger.console("-" * 78)
