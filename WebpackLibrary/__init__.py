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

    def __init__(self):
        """WebpackLibrary can be imported with optional arguments.
        """
        pass

    def start_webpack(self,
                      command,
                      path='.',
                      check_webpack_output_for_string='bundle is now VALID',
                      debug=False):
        """Start Webpack Dev Server."""
        # import sys
        # import pdb
        # for attr in ('stdin', 'stdout', 'stderr'):
        #     setattr(sys, attr, getattr(sys, '__%s__' % attr))
        # pdb.set_trace()
        try:
            self.path = os.path.realpath(path)
        except:
           logger.console('ERROR: File not found in path: {}'.format(path))

        if isinstance(debug, str) and debug.lower() == 'true':
            self.debug = True
        else:
            self.debug = False

        try:
            args = command.split(' ')
            self.webpack_process = subprocess.Popen(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=1,
                cwd=self.path,
            )
        except OSError as e:
            logger.console('ERROR: Starting Webpack failed with: {}'.format(e))

        if not getattr(self, 'webpack_process', False):
            print('\n\n')  # noqa
            print('ERROR: Starting Webpack failed with:\n')  # noqa
            print(e)  # noqa
            print('\n')  # noqa
            exit(1)

        if self.webpack_process.returncode == 1:
            print('\n\n')  # noqa
            print('ERROR: Starting Webpack failed with exit code: {}\n'.format(  # noqa
                self.webpack_process.returncode
            ))
            print(self.webpack_process.communicate('n\n')[0])  # noqa
            print('\n')  # noqa
            exit(1)

        self.webpack_pid = self.webpack_process.pid
        if self.debug:
            logger.console(
                "Webpack process started (PID: %s)" % self.webpack_pid,
            )
        stdout = []
        with self.webpack_process.stdout:
            for line in iter(self.webpack_process.stdout.readline, b''):
                if self.debug:
                    logger.console(line)
                    stdout.append(line)
                if check_webpack_output_for_string in line:
                    if self.debug:
                        logger.console(
                            "Webpack process ready (PID: %s)" %
                            self.webpack_pid,
                        )
                    break

    def stop_webpack(self):
        """Stop Webpack Dev server."""
        os.kill(self.webpack_pid, signal.SIGKILL)
        if self.debug:
            logger.console(
                "Webpack process stopped (PID: %s)" % self.webpack_pid,
            )
