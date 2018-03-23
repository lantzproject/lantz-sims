# -*- coding: utf-8 -*-
"""
    lantz.simulators
    ~~~~~~~~~~~~~~~~

    Instrument simulators for testing.

    :copyright: 2015 by The Lantz Authors
    :license: BSD, see LICENSE for more details.
"""

#: Dict connecting simulator name with main callable.
SIMULATORS = {}

import logging

from . import fungen, experiment, voltmeter


def main(args=None):
    """Run simulators.
    """
    import argparse

    parser = argparse.ArgumentParser(description='Run Lantz simulators.')
    parser.add_argument('simulator', choices=list(SIMULATORS.keys()))
    args, pending = parser.parse_known_args(args)
    print('Dispatching ' + args.simulator)

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%Y-%d-%m %H:%M:%S')

    SIMULATORS[args.simulator](pending)
